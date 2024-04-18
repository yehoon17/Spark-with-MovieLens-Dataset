import argparse
from pyspark.sql import SparkSession
from analysis import top_movies


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Spark Project")
    parser.add_argument("-t", "--time", action="store_true", help="Display execution time")
    args = parser.parse_args()

    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("SparkProject") \
        .getOrCreate()

    # Load dataset
    ratings_df = spark.read.csv("data/ratings.csv", header=True, inferSchema=True)

    # Execute top movies analysis
    top_movies.analyze_top_movies(ratings_df, is_timer=args.time)

    # Stop SparkSession
    spark.stop()

if __name__ == "__main__":
    main()
