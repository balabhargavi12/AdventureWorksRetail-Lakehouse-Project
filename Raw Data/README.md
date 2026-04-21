# 📂 Raw Data – AdventureWorks Lakehouse Project

## 📌 Overview
This folder contains the raw datasets used in the AdventureWorks Retail Lakehouse project.

The data is stored in its original format and is used as input for the Bronze layer of the pipeline.

---

## 📊 Dataset Description
The dataset represents a retail business and includes multiple related tables:

- **Sales** – Transaction and order details  
- **Customers** – Customer information  
- **Products** – Product details and pricing  
- **Categories & Subcategories** – Product classification  
- **Calendar** – Date and time-related data  
- **Returns** – Returned products data  
- **Territories** – Sales regions and locations  

---

## 📁 File Format
- Data is stored in **CSV format**  
- Loaded into Databricks using PySpark  
- Schema is inferred during ingestion  

---

## 🎯 Purpose
- Provide raw input data for the pipeline  
- Used to build **Bronze → Silver → Gold layers**  
- Simulates real-world retail data scenarios  

---

## ⚠️ Data Characteristics
- Contains:
  - Missing values  
  - Duplicate records  
  - Inconsistent data  
- Requires cleaning and transformation in later stages  

---

## 🔄 Usage in Project
- Used in **Bronze Layer** for data ingestion  
- Further processed in **Silver Layer**  
- Aggregated in **Gold Layer** for insights  

---

## 📌 Note
- Data is not modified in this folder  
- All transformations are handled in pipeline layers  
- Represents real-world data challenges for learning  

---

## ✅ Outcome
This raw data serves as the foundation for building a complete data pipeline and generating business insights.
