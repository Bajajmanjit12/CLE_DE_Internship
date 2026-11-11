
import pandas as pd
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def ingest(input_path, output_path):

    try:
        # 1. Read CSV file
        logging.info("Reading input CSV file...")
        df = pd.read_csv(input_path)

        logging.info("Loaded %d rows.", len(df))

        # 2. Clean column names
        logging.info("Cleaning column names...")
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        # 3. Remove duplicate records
        logging.info("Removing duplicate records...")
        duplicates = df.duplicated().sum()
        df = df.drop_duplicates()

        logging.info("Removed %d duplicate rows.", duplicates)

        # 4. Handle missing Order IDs
        logging.info("Handling missing values...")

        rows_before = len(df)
        df = df.dropna(subset=["order_id"])
        logging.info(
            "Removed %d rows with missing Order IDs.",
            rows_before - len(df)
        )

        # Fill other missing values
        df["customer_name"] = df["customer_name"].fillna("Unknown")
        df["city"] = df["city"].fillna("Unknown")

        # 5. Fix data types
        logging.info("Converting data types...")

        df["amount"] = pd.to_numeric(
            df["amount"], errors="coerce"
        ).fillna(0.0)

        df["order_date"] = pd.to_datetime(
            df["order_date"],
            errors="coerce",
            dayfirst=True,
            format="mixed"
        )

        # Check for invalid dates
        if df["order_date"].isna().any():
            raise ValueError("Invalid or missing order dates found!")

        # 6. Validate amounts
        logging.info("Validating amounts...")

        if (df["amount"] < 0).any():
            raise ValueError("Negative amounts found!")

        logging.info("Amount validation successful.")

        # 7. Save as Parquet
        logging.info("Saving cleaned data as Parquet...")

        Path(output_path).parent.mkdir(
            parents=True, exist_ok=True
        )

        df.to_parquet(output_path, index=False)

        logging.info("Parquet file saved successfully!")
        logging.info("Final row count: %d", len(df))

        return df

    except FileNotFoundError:
        logging.error("Input file not found: %s", input_path)
        raise

    except Exception as e:
        logging.exception("Data ingestion failed: %s", e)
        raise


# Run the ingestion function
if __name__ == "__main__":
    ingest(
        "messy_orders.csv",
        "cleaned_orders.parquet"
    )
