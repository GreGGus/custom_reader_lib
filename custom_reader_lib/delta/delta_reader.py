from pyspark.sql import SparkSession

def read_delta_table(name):
    spark = SparkSession.builder.getOrCreate()
    return spark.read.table(name)
