"""
Main CLI or app entry point
"""

from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


def main():
    # Extract data
    extract()

    # Start Spark session
    spark = start_spark("USBirthDataProcessing")

    # Load data into DataFrame
    df = load_data(spark)

    # Example metrics
    describe(df)

    # Query the data
    query(
        spark,
        df,
        (
            "SELECT year, COUNT(*) AS birth_count "
            "FROM USBirthData "
            "GROUP BY year "
            "ORDER BY year"
        ),
        "USBirthData",
    )

    # Example transformation
    example_transform(df)

    # End Spark session
    end_spark(spark)


if __name__ == "__main__":
    main()
