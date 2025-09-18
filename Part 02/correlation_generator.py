import pandas as pd

data = pd.read_parquet(
    path=r"./datasets/clean_data.parquet",
    engine="pyarrow",
)

threshold = data["TotalRatingCount"].quantile(0.80)

rating_popular_movie = data.query(f"TotalRatingCount > {threshold}")
movieMath = rating_popular_movie.pivot_table(
    index="userId", columns="title", values="rating"
)

movie_corr = movieMath.corr()
movie_corr.to_parquet(
    path=r"./datasets/correlation_data.parquet", engine="pyarrow", index=True
)
