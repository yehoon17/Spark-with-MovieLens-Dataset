from pyspark.sql import SparkSession
from analysis import analyze_top_movies, analyze_user_trands

def main():
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("SparkProject") \
        .getOrCreate()

    # Load dataset
    ratings_df = spark.read.csv("data/ratings.csv", header=True, inferSchema=True)
    movies_df = spark.read.csv("data/movies.csv", header=True, inferSchema=True)

    # Analysis
    analyze_top_movies(ratings_df, movies_df)
    # analyze_user_trands(ratings_df)

    # Stop SparkSession
    spark.stop()

if __name__ == "__main__":
    main()
