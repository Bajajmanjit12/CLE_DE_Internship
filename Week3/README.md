# Celebal Learning Engagement Program – Data Engineering Internship

**Repository:** [CLE_DE_Internship](https://github.com/Bajajmanjit12/CLE_DE_Internship)

## Objective

The objective of this repository is to document and maintain the practical assignments, hands-on exercises, and learning outcomes completed as part of the **Celebal Learning Engagement Program (CLE) – Data Engineering Internship**.

This repository focuses on developing practical Data Engineering skills through Python programming, data processing, data cleaning, file handling, and other technologies used in real-world data workflows.

## Week 3 – Python for Data Engineers

### Assignment: CSV Data Ingestion and Cleaning

The objective of this assignment was to develop a reusable Python script to ingest, clean, validate, and transform a messy CSV dataset into a structured Parquet file.

### Tasks Performed

The following operations were implemented as part of the assignment:

1. **CSV Data Ingestion:** Read the input CSV dataset using the Pandas library.
2. **Column Name Standardization:** Converted column names into lowercase and replaced spaces with underscores.
3. **Duplicate Removal:** Identified and removed duplicate records to maintain data consistency.
4. **Missing Value Handling:** Identified null values, removed records with missing IDs, and handled other missing values using appropriate default values.
5. **Data Type Conversion:** Converted columns into their appropriate data types, including numeric and date columns.
6. **Data Validation:** Checked for negative amounts and raised an error when invalid values were found.
7. **Parquet Conversion:** Saved the cleaned dataset in Parquet format for efficient storage and further processing.
8. **Logging and Exception Handling:** Used logging to track processing steps and exception handling to manage errors such as missing input files.

### Technologies and Libraries

- **Python** – Programming language used to implement the ingestion workflow.
- **Pandas** – Used for data manipulation, cleaning, and transformation.
- **PyArrow** – Used to support Parquet file storage.
- **Logging** – Used to track execution and processing steps.
- **Exception Handling** – Used to handle errors gracefully.

## Project Structure

```text
CLE_DE_Internship/
│
├── README.md
│
└── Week3/
    │
    ├── messy_orders.csv
    ├── main.py
    ├── cleaned_orders.parquet
    └──README.md
```

### File Description

| File / Folder | Description |
|---|---|
| `Week3/` | Contains Week 3 assignment files. |
| `messy_orders.csv` | Input dataset containing intentionally inconsistent and missing values. |
| `ingest.py` | Python script for data ingestion, cleaning, validation, and transformation. |
| `cleaned_orders.parquet` | Output file containing the processed dataset. |
| `README.md` | Documentation describing the repository and assignment. |

## How to Run the Assignment

**1. Clone the repository**

```bash
git clone https://github.com/Bajajmanjit12/CLE_DE_Internship.git
```

**2. Navigate to the Week 2 folder**

```bash
cd CLE_DE_Internship/Week2
```

**3. Install the required libraries**

```bash
pip install pandas pyarrow
```

**4. Execute the Python script**

```bash
python main.py
```

**5. Verify the output**

After successful execution, the cleaned dataset will be saved as:

```text
cleaned_orders.parquet
```

## Learning Outcomes

Through this assignment, I gained practical experience in:

- Working with CSV datasets using Python and Pandas.
- Understanding data quality issues and data preprocessing.
- Handling missing values and duplicate records.
- Performing data type conversions and validation.
- Working with Parquet file formats.
- Building reusable data ingestion scripts.
- Implementing logging and exception handling in data workflows.

---

**Note:** This repository will be updated with subsequent weekly assignments and practical work completed during the Celebal Data Engineering Internship.