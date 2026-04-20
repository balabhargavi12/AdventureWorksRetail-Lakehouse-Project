from pyspark import pipelines as dp
from pyspark.sql.functions import *


@dp.materialized_view()
def silver_customers():
    return spark.read.table("bronze_customers") \
        .dropDuplicates() \
        .withColumn("CustomerName", concat_ws(" ", col("FirstName"), col("LastName"))) \
        .fillna({"CustomerName": "Unknown"})

@dp.materialized_view()
def silver_products():
    return spark.read.table("bronze_products") \
        .dropDuplicates() \
        .withColumn("ProductPrice", col("ProductPrice").cast("double")) \
        .fillna({"ProductName": "Unknown"})

@dp.materialized_view()
def silver_calendar():
    return spark.read.table("bronze_calendar") \
        .dropDuplicates() \
        .withColumn("Date", to_date(col("Date"))) \
        .withColumn("Year", year(col("Date"))) \
        .withColumn("Month", month(col("Date")))

@dp.materialized_view()
def silver_sales():
    return spark.read.table("bronze_sales") \
        .dropDuplicates() \
        .withColumn("OrderDate", to_date(col("OrderDate"))) \
        .withColumn("OrderQuantity", col("OrderQuantity").cast("int"))

@dp.materialized_view()
def silver_subcategories():
    return spark.read.table("bronze_subcategories") \
        .dropDuplicates() \
        .fillna({"SubcategoryName": "Unknown"})

@dp.materialized_view()
def silver_categories():
    return spark.read.table("bronze_categories") \
        .dropDuplicates() \
        .fillna({"CategoryName": "Unknown"})

@dp.materialized_view()
def silver_returns():
    return spark.read.table("bronze_returns") \
        .dropDuplicates() \
        .withColumn("ReturnDate", to_date(col("ReturnDate"))) \
        .withColumn("ReturnQuantity", col("ReturnQuantity").cast("int"))

@dp.materialized_view()
def silver_territories():
    return spark.read.table("bronze_territories") \
        .dropDuplicates() \
        .fillna({"Region": "Unknown"})

@dp.materialized_view()
def silver_sales_enriched():
    sales = spark.read.table("silver_sales")
    customers = spark.read.table("silver_customers")
    products = spark.read.table("silver_products")
    calendar = spark.read.table("silver_calendar")
    sub = spark.read.table("silver_subcategories")
    cat = spark.read.table("silver_categories")
    terr = spark.read.table("silver_territories")

    return sales \
        .join(customers, "CustomerKey", "left") \
        .join(products, "ProductKey", "left") \
        .join(sub, "ProductSubcategoryKey", "left") \
        .join(cat, "ProductCategoryKey", "left") \
        .join(terr, sales["TerritoryKey"] == terr["SalesTerritoryKey"], "left") \
        .join(calendar, sales["OrderDate"] == calendar["Date"], "left") \
        .withColumn("SalesAmount", col("OrderQuantity") * col("ProductPrice")) \
        .fillna({"SalesAmount": 0})