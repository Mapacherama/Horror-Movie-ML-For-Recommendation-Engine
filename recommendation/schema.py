import graphene 

from src.data_processing import get_similar_movies

class MovieType(graphene.ObjectType):
    title = graphene.String()
    movie_id = graphene.Int()

class Query(graphene.ObjectType):
    similar_movies = graphene.List(MovieType, target_movie_title=graphene.String(), N=graphene.Int())    

    def resolve_similar_movies(self, info, target_movie_title, N=10):
        similar_movies = get_similar_movies(target_movie_title, N)
        return similar_movies