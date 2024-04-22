from pyspark.sql.functions import col, count, avg, expr, explode, split, from_unixtime, window


def analyze_top_movies(ratings_df, movies_df):
    # Join ratings_df with movies_df to get movie titles and genres
    movie_ratings_df = ratings_df.join(movies_df, "movieId")

    # Calculate the average rating and number of ratings for each movie
    movie_stats_df = (
        movie_ratings_df
        .groupBy("movieId", "title", "genres") 
        .agg(
            count("rating").alias("num_ratings"),
            avg("rating").alias("avg_rating")
            )
        )

    # Calculate a weighted average rating based on the number of ratings
    expr_ = "avg_rating * num_ratings / (num_ratings + 10) + 5 * 10 / (num_ratings + 10)"
    weighted_avg_df = movie_stats_df.withColumn("weighted_avg_rating", expr(expr_))
    
    # Order the movies by weighted average rating and number of ratings
    top_movies_df = weighted_avg_df.orderBy(
        col("weighted_avg_rating").desc(),
        col("num_ratings").desc()
        )

    # Display top N movies
    print("Top 10 Movies by Weighted Average Rating and Number of Ratings:")
    cols = ["title", "genres", "weighted_avg_rating", "num_ratings"]
    top_movies_df.select(cols).show(10, truncate=False)

def analyze_user_trands(ratings_df):
    # Convert timestamp to a timestamp type
    ratings_df = ratings_df.withColumn("timestamp", from_unixtime("timestamp"))

    # Group ratings by user and time window
    user_trends_df = (
        ratings_df
        .groupBy("userId", window("timestamp", "1 week"))
        .avg("rating")
    )

    # Order the user trends by userId and window
    user_trends_df = user_trends_df.orderBy("userId", "window")

    # Display user trends
    print("User Rating Trends:")
    user_trends_df.show(truncate=False)
