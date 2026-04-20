from pyspark import pipelines as dp
from pyspark.sql.functions import *

# -------------------------
# BASE
# -------------------------
def get_silver():
    return spark.read.table("silver_sales_enriched")


# -------------------------
# KPI SUMMARY
# -------------------------
@dp.materialized_view()
def kpi_summary():
    df = get_silver()

    return df.agg(
        sum("SalesAmount").alias("TotalRevenue"),
        countDistinct("CustomerKey").alias("TotalCustomers"),
        countDistinct("ProductKey").alias("TotalProducts")
    )


# -------------------------
# KPI DAILY TREND
# -------------------------
@dp.materialized_view()
def kpi_daily_trend():
    df = get_silver()

    return df.groupBy("OrderDate") \
        .agg(sum("SalesAmount").alias("Revenue")) \
        .orderBy("OrderDate")


# -------------------------
# KPI MONTHLY TREND
# -------------------------
@dp.materialized_view()
def kpi_monthly_trend():
    df = get_silver()

    return df.groupBy("Year", "Month") \
        .agg(sum("SalesAmount").alias("Revenue")) \
        .orderBy("Year", "Month")


# -------------------------
# KPI TOP PRODUCTS
# -------------------------
@dp.materialized_view()
def kpi_top_products():
    df = get_silver()

    return df.groupBy("ProductName") \
        .agg(sum("SalesAmount").alias("Revenue")) \
        .orderBy(desc("Revenue")) \
        .limit(10)


# -------------------------
# KPI TOP CUSTOMERS
# -------------------------
@dp.materialized_view()
def kpi_top_customers():
    df = get_silver()

    return df.groupBy("CustomerName") \
        .agg(sum("SalesAmount").alias("Revenue")) \
        .orderBy(desc("Revenue")) \
        .limit(10)


# -------------------------
# KPI SUBCATEGORY PERCENTAGE
# -------------------------
@dp.materialized_view()
def kpi_subcategory_percentage():
    # Read from pipeline dataset using get_silver and recalculate
    df = get_silver()
    
    # Calculate subcategory revenue
    df_subcategory = df.groupBy("SubcategoryName") \
        .agg(
            sum("SalesAmount").alias("revenue"),
            count("*").alias("order_count")
        )
    
    # Calculate total revenue for percentage
    total_revenue_df = df.selectExpr("sum(SalesAmount) as total_revenue")
    total_revenue = total_revenue_df.collect()[0]["total_revenue"]
    
    # Add percentage column
    return df_subcategory \
        .withColumn("percentage", round((col("revenue") / lit(total_revenue)) * 100, 1)) \
        .orderBy(desc("revenue"))