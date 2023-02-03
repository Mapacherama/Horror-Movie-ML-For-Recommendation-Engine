from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/recommend/<user_id>', methods=['GET'])
def recommend(user_id):
    # Load the user-item interaction data
    df = pd.read_csv("interactions.csv")

    # Calculate the average movie rating for each user
    user_mean = df.groupby(by="user_id")["rating"].mean()

    # Calculate the average rating for each movie
    item_mean = df.groupby(by="movie_id")["rating"].mean()

    # Calculate the deviation of each rating from the mean rating for each user
    df["user_deviation"] = df["rating"] - user_mean[df["user_id"]]

    # Calculate the deviation of each rating from the mean rating for each movie
    df["item_deviation"] = df["rating"] - item_mean[df["movie_id"]]

    # Calculate the weighted average of the user deviation and item deviation
    df["hybrid_rating"] = (df["user_deviation"] + df["item_deviation"]) / 2

    # Sort the ratings in descending order and recommend the top N movies
    N = 10
    df = df.sort_values(by="hybrid_rating", ascending=False)
    recommendations = df.head(N)["movie_id"]

    return jsonify({"recommendations": recommendations})