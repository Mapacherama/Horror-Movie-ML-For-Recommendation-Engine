import pandas as pd
import numpy as np
import uuid

df = pd.read_csv("../data/raw/IMDB_Horror_movies.csv")

column_mapping = {
    "Title": "title",
    "Genres": "genres",
    "Release Date": "release_date",
    "Release Country": "release_country",
    "Movie Rating": "movie_rating",
    "Review Rating": "review_rating",
    "Movie Run Time": "movie_run_time",
    "Plot": "plot",
    "Cast": "cast",
    "Language": "language",
    "Filming Locations": "filming_locations",
    "Budget": "budget"
}

df.rename(columns=column_mapping, inplace=True)

# Add a new column 'movie_id' to the data frame
df.insert(0, 'movie_id', range(1, 1+len(df)))

df['review_rating'] = df['review_rating'].astype(float)

print(df['review_rating'].isnull().sum())

# Replace missing values in the movie_rating column with the mean of the column
mean_rating = df['review_rating'].mean()
df['review_rating'].fillna(mean_rating, inplace=True)

# Check for missing values again to confirm that they have been replaced
print(df['review_rating'].isnull().sum())

df.to_csv("cleaned_horror_movie_list_V4.csv", index=False)