import pandas as pd

data = pd.read_parquet(
    path=r"./datasets/correlation_data.parquet",
    engine="pyarrow",
)


def get_similar_movies(movie_name: str):
    if movie_name in data.columns:
        similar_movies = data[movie_name].sort_values(ascending=False)[1:]
        return similar_movies
    else:
        return f"Movie '{movie_name}' not found in the dataset."


if __name__ == "__main__":
    movie_name = "Pulp Fiction (1994)"
    similar_movies = get_similar_movies(movie_name)
    print(f"Top movies similar to '{movie_name}':\n{similar_movies}")
