from pyspark.sql import SparkSession
from analysis import top_movies

def main():
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("SparkProject") \
        .getOrCreate()

    # Load dataset
    ratings_df = spark.read.csv("data/ratings.csv", header=True, inferSchema=True)

    # Execute top movies analysis
    top_movies.analyze_top_movies(spark, ratings_df)

    # Stop SparkSession
    spark.stop()

if __name__ == "__main__":
    main()
