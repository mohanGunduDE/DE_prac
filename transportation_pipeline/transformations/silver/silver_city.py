from pyspark import pipelines as pd
from pyspark.sql.functions import *

@pd.materialized_view(
    name = "transportation.silver.city"
)
def city():
    df_bronze = spark.read.table("transportation.bronze.city")
    df_silver = df_bronze.withColumnRenamed("ingest_time","bronze_ingestion")\
                     .withColumn("silver_ingestion",current_timestamp())  
    return df_silver
