from pyspark import pipelines as dp
from pyspark.sql import functions as F

dataset_path = spark.conf.get("dataset_path")

@dp.table(
    name = "bronze",
    partition_cols=["topic", "year_month"],
    table_properties={
        "delta.appendOnly": "true",
        "pipelines.reset.allowed": "false",
    }
)
def process_bronze():
    schema = "key BINARY, value BINARY, topic STRING, partition LONG, offset LONG, timestamp LONG"
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .schema(schema)
        .load(f"{dataset_path}/kafka-raw-etl")
        .withColumn("timestamp", (F.col("timestamp")/1000).cast("timestamp"))  
        .withColumn("year_month", F.date_format("timestamp", "yyyy-MM"))
    )


@dp.temporary_view()
def country_lookup():
    return(spark.read.json(f"{dataset_path}/country_lookup"))