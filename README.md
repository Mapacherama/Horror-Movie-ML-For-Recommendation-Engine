# Hybrid Movie Recommender System

This project implements a hybrid movie recommender system that combines the strengths of both collaborative filtering and content-based filtering to make recommendations.

## Requirements

    Python 3.x
    Pandas

## Getting Started

1. Clone the repository to your local machine:

         $ git clone https://github.com/<your-username>/hybrid-movie-recommender.git

2. Change into the project directory:

        $ cd hybrid-movie-recommender

3. Install the required libraries using pip:

        $ pip install -r requirements.txt

4. Run the recommendation script:

        $ python recommender.py

## Input Data

The input data for the recommendation system is a csv file named interactions.csv, which contains the user-item interaction data, with columns for user_id, movie_id, and rating.

## Output

The recommendation script outputs the recommended movies for each user based on the hybrid rating calculated using the weighted average of the user deviation and item deviation.

## License

This project is licensed under the MIT License.
