import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the user-item interaction data
df = pd.read_csv("cleaned_horror_movie_list_V4.csv")

# Extract the features to use for recommendations
features = ['movie_id', 'title', 'genres', 'cast', 'plot']
df = df[features]

# Fill any missing values in the data
df.fillna("", inplace=True)

df['combined_features'] = df.apply(lambda x: x['title'] + " " + x['genres'] + " " + x['cast'] + " " + x['plot'], axis=1)

# Use TfidfVectorizer to create a matrix of movie feature vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined_features'])

# Compute the cosine similarity between each movie
similarity_matrix = cosine_similarity(tfidf_matrix)

# Convert the similarity matrix into a pandas dataframe
similarity_df = pd.DataFrame(similarity_matrix, index=df.index, columns=df.index)

def get_similar_movies(target_movie_title, N=10):
    # Create a mapping from movie titles to movie IDs
    title_to_id = df.set_index("title")["movie_id"]
    
    # Get the target movie ID from the title
    target_movie_id = title_to_id[target_movie_title]
    
    # Compute the similarity scores for the target movie based on its title
    similarity_scores = similarity_df[target_movie_id].sort_values(ascending=False)
    similar_movies_ids = similarity_scores.index[1:N+1]
    
    # Map the similar movie IDs back to their titles
    similar_movies_titles = df[df["movie_id"].isin(similar_movies_ids)]["title"]
    
    return similar_movies_titles

# Example usage: get the top 10 most similar movies to the movie with index 0
top_10 = get_similar_movies('The Visitor (2016)', 10)
print(top_10)
