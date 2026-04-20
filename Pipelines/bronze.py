from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# File path (adjust if needed)
base_path = "dbfs:/Volumes/adventureworks-lakehouse-project/adventureworks/adventureworksdata/"

# -------------------------
# BRONZE: RAW DATA INGESTION
# -------------------------

@dp.materialized_view()
def bronze_sales():
    return spark.read.csv(f"{base_path}AdventureWorks_Sales_2015.csv", header=True, inferSchema=True)

@dp.materialized_view()
def bronze_customers():
    return spark.read.csv(f"{base_path}AdventureWorks_Customers.csv", header=True, inferSchema=True)

@dp.materialized_view()
def bronze_products():
    return spark.read.csv(f"{base_path}AdventureWorks_Products.csv", header=True, inferSchema=True)

@dp.materialized_view()
def bronze_calendar():
    return spark.read.csv(f"{base_path}AdventureWorks_Calendar.csv", header=True, inferSchema=True)

@dp.materialized_view()
def bronze_subcategories():
    return spark.read.csv(f"{base_path}AdventureWorks_Product_Subcategories.csv", header=True, inferSchema=True)

@dp.materialized_view()
def bronze_categories():
    return spark.read.csv(f"{base_path}AdventureWorks_Product_Categories.csv", header=True, inferSchema=True)

@dp.materialized_view()
def bronze_returns():
    return spark.read.csv(f"{base_path}AdventureWorks_Returns.csv", header=True, inferSchema=True)

@dp.materialized_view()
def bronze_territories():
    return spark.read.csv(f"{base_path}AdventureWorks_Territories.csv", header=True, inferSchema=True)
