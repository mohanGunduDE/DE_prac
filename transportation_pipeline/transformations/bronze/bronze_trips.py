from pyspark import pipelines as dp
from pyspark.sql.functions import *

source = "/Volumes/transportation/bronze/source_data/trips"

@dp.table(
    name = "transportation.bronze.trip",
       table_properties={
        "quality": "bronze",
        "layer": "bronze",
        "source_format": "csv",
        "delta.enableChangeDataFeed": "true",
        "delta.autoOptimize.optimizeWrite": "true",
        "delta.autoOptimize.autoCompact": "true",
    },
)
def func():
    df = spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .option("coludFiles.maxFilesPerTrigger","100")\
        .option("cloudFiles.schemaEvolutionMode", "rescue")\
        .load(source)
    

    df = df.withColumn("ingest_time", current_timestamp())\
           .withColumn("file_name",col("_metadata.file_path"))\
           .withColumnRenamed("distance_travelled(km)","distance_travelled")
    return df

