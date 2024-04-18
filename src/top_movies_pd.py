import pandas as pd
import time

# Load dataset
ratings_df = pd.read_csv("data/ratings.csv")

# Start time
start_time = time.time()

# Calculate average rating for each movie
average_ratings_df = ratings_df.groupby("movieId")["rating"].mean()

# Sort average ratings and get top 10
top_10_ratings = average_ratings_df.sort_values(ascending=False).head(10)

# Print top 10 average ratings
print("Top 10 Average Ratings:")
print(top_10_ratings)

# End time
end_time = time.time()

# Print execution time
print("Execution time (pandas):", end_time - start_time)
