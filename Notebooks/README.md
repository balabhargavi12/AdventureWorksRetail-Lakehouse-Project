
# 📓 Databricks Notebooks – AdventureWorks Lakehouse Project

## 📌 Overview
This folder contains Databricks notebooks used to build and execute the **end-to-end data pipeline** for the AdventureWorks Retail project.

The notebooks follow the **Medallion Architecture (Bronze → Silver → Gold)** and demonstrate step-by-step data processing using PySpark.

---

## 🥉 Bronze Layer Notebook
- Loads raw data from source files (CSV)  
- Stores data in tables without any transformation  
- Acts as the starting point of the pipeline  

👉 Purpose: Capture raw data as-is  

---

## 🥈 Silver Layer Notebook
- Cleans and processes raw data  
- Handles:
  - Null values  
  - Duplicate records  
  - Data type conversions  
- Joins multiple datasets  
- Creates enriched dataset (sales_enriched)  

👉 Purpose: Create clean and structured data  

---

## 🥇 Gold Layer Notebook
- Performs aggregations and analysis  
- Generates KPIs such as:
  - Total Revenue  
  - Sales Trends  
  - Top Customers  
  - Top Products  
- Produces dashboard-ready data  

👉 Purpose: Generate business insights  

---

## 🔄 Workflow
1. Run Bronze notebook → Load raw data  
2. Run Silver notebook → Clean & transform data  
3. Run Gold notebook → Generate insights  

---

## ⚙️ Technologies Used
- Databricks Notebooks  
- PySpark  
- SQL  
- Delta Lake  

---

## 🔑 Key Features
- Step-by-step data pipeline execution  
- Data cleaning and transformation  
- Join operations across multiple tables  
- KPI generation for analytics  
- Ready for visualization tools  

---

## ✅ Outcome
The notebooks demonstrate how raw data is converted into **clean, structured, and analytics-ready datasets** using Databricks.

---

## 📌 Note
- Notebooks are designed for learning and demonstration  
- Can be executed independently or as part of a pipeline  
