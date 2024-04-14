def analyze_top_movies(spark, ratings_df):
    # Calculate average rating for each movie
    average_ratings_df = ratings_df.groupBy("movieId").avg("rating").alias("avg_rating")

    # Find top N movies by average rating
    top_movies_df = average_ratings_df.orderBy("avg(rating)", ascending=False).limit(10)

    # Display top N movies
    print("Top 10 Movies by Average Rating:")
    top_movies_df.show()
