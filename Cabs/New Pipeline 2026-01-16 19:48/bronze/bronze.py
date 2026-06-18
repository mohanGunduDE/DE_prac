from pyspark import pipelines as dp
from pyspark.sql.functions import *


@dp.materialized_view(name="emp_table")
def emp_table():
    return spark.read.table("employees_bronze")

    

