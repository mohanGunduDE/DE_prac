from pyspark import pipelines as pd
from pyspark.sql.functions import *

source = "/Volumes/transportation/bronze/source_data/city/city.csv"

@pd.materialized_view()
def city():
    df = spark.read.format("csv").option("header","true").load(source)
    df = df.withColumn("file_name",col("_metadata.file_path")).withColumn("ingest_time",current_timestamp())
    return df
