# 🔄 Data Pipelines – AdventureWorks Lakehouse Project

## 📌 Overview
This folder contains ETL pipeline scripts built using PySpark in Databricks.  
The pipelines follow the **Medallion Architecture (Bronze → Silver → Gold)** to process data step by step.

---

## 🥉 Bronze Layer (`bronze.py`)
- Loads raw data from CSV files stored in DBFS  
- Creates tables like:
  - sales, customers, products, calendar, categories, etc.  
- No transformations applied (raw data)  

👉 Purpose: Store original data safely :contentReference[oaicite:0]{index=0}  

---

## 🥈 Silver Layer (`silver.py`)
- Cleans and transforms data:
  - Removes duplicates  
  - Handles null values  
  - Converts data types  
- Creates new columns (e.g., CustomerName)  
- Joins multiple tables to create **sales_enriched** dataset  
- Calculates **SalesAmount**

👉 Purpose: Create clean and structured data :contentReference[oaicite:1]{index=1}  

---

## 🥇 Gold Layer (`gold.py`)
- Generates business insights (KPIs):
  - Total Revenue  
  - Daily & Monthly trends  
  - Top Customers  
  - Top Products  
  - Subcategory percentage  
- Uses aggregations and grouping  

👉 Purpose: Create analytics-ready data for dashboards :contentReference[oaicite:2]{index=2}  

---

## 🔄 Pipeline Flow
1. Run `bronze.py` → Load raw data  
2. Run `silver.py` → Clean & join data  
3. Run `gold.py` → Generate insights  

---

## ⚙️ Technologies Used
- PySpark  
- Databricks  
- Delta Live Tables (Materialized Views)  

---

## ✅ Outcome
This pipeline converts raw retail data into **clean, enriched, and analytics-ready datasets** for reporting and decision-making.

---

## 📌 Note
- Pipelines are implemented using **materialized views**  
- Designed for scalability and real-world data processing  

