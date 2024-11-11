import os
import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


def start_spark(app_name="MyApp"):
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    return spark


def end_spark(spark):
    spark.stop()


def extract():
    # Set a relative path for the data file
    data_path = os.path.join(os.path.dirname(__file__), "../data/US_birth.csv")
    if os.path.exists(data_path):
        return data_path
    else:
        raise FileNotFoundError(f"The file {data_path} does not exist.")


def load_data(spark):
    data_path = extract()
    schema = StructType(
        [
            StructField("year", IntegerType(), True),
            StructField("month", StringType(), True),
            StructField("day", IntegerType(), True),
            StructField("births", IntegerType(), True),
        ]
    )
    df = spark.read.option("header", "true").schema(schema).csv(data_path)
    return df


def describe(df):
    df.describe().show()


def query(spark, df, sql_query, table_name):
    df.createOrReplaceTempView(table_name)
    result = spark.sql(sql_query)
    result.show()


def example_transform(df):
    df = df.withColumn("day_of_week", (F.col("day") % 7) + 1)
    df.show()
