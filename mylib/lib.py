"""
library functions
"""

import os
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

from pyspark.sql.types import StructType, StructField, IntegerType

LOG_FILE = "pyspark_output.md"


def log_output(operation, output, query=None):
    """Adds output information to a markdown file."""
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query:
            file.write(f"The query is {query}\n\n")
        file.write("The truncated output is: \n\n")
        file.write(output)
        file.write("\n\n")


def start_spark(appName):
    """Starts a Spark session with the specified application name."""
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark


def end_spark(spark):
    """Stops the Spark session."""
    spark.stop()
    return "stopped spark session"


def extract(
    url=None,
    file_path="/Users/liuliangcheng/Desktop/Duke/IDS_DE/ids_de_mini10/data/US_birth.csv",
    directory="data",
):
    """Extracts a file from a URL or uses a local path if available."""
    # If the file already exists locally, skip downloading
    if os.path.exists(file_path):
        return file_path

    # If a URL is provided, download the file
    if url:
        # Ensure the directory exists
        if not os.path.exists(directory):
            os.makedirs(directory)

        with requests.get(url) as r:
            r.raise_for_status()  # Ensure download was successful
            with open(file_path, "wb") as f:
                f.write(r.content)

    return file_path


def load_data(
    spark,
    data="/Users/liuliangcheng/Desktop/Duke/IDS_DE/ids_de_mini10/data/US_birth.csv",
    name="USBirthData",
):
    """Loads data into a Spark DataFrame with the appropriate schema."""
    # Set schema for US_birth.csv
    schema = StructType(
        [
            StructField("year", IntegerType(), True),
            StructField("month", IntegerType(), True),
            StructField("date_of_month", IntegerType(), True),
            StructField("day_of_week", IntegerType(), True),
            StructField("births", IntegerType(), True),
        ]
    )

    df = spark.read.option("header", "true").schema(schema).csv(data)

    log_output("load data", df.limit(10).toPandas().to_markdown())

    return df


def query(spark, df, query, name):
    """Executes a SQL query using Spark SQL."""
    df = df.createOrReplaceTempView(name)

    log_output("query data", spark.sql(query).toPandas().to_markdown(), query)

    return spark.sql(query).show()


def describe(df):
    """Generates descriptive statistics for the DataFrame."""
    summary_stats_str = df.describe().toPandas().to_markdown()
    log_output("describe data", summary_stats_str)

    return df.describe().show()


def example_transform(df):
    """Performs an example transformation on the DataFrame."""
    # Example transformation to categorize days as 'Weekend' or 'Weekday'
    conditions = [
        (col("day_of_week") == 1)
        | (col("day_of_week") == 7),  # Assuming 1 = Sunday, 7 = Saturday
    ]

    categories = ["Weekend", "Weekday"]

    df = df.withColumn(
        "Day_Type", when(conditions[0], categories[0]).otherwise(categories[1])
    )

    log_output("transform data", df.limit(10).toPandas().to_markdown())

    return df.show()
