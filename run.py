import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


print("=" * 60)
print("MOVIE RECOMMENDATION SYSTEM".center(60))
print("=" * 60)


try:
    df = pd.read_csv("outputs/processed_movies.csv")
except FileNotFoundError:
    print("\nprocessed_movies.csv not found.")
    print("Run the notebook first.")
    exit()


print("\nLoading recommendation model...")

tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words='english'
)

vectors = tfidf.fit_transform(
    df['tags']
).toarray()

similarity = cosine_similarity(vectors)

print("Model loaded successfully.")


def recommend(movie_name):

    movie_name = movie_name.lower()

    matches = df[
        df['title'].str.lower() == movie_name
    ]

    if matches.empty:
        print("\nMovie not found.")
        return

    movie_index = matches.index[0]

    input_movie = df.iloc[movie_index]

    print("\n" + "=" * 60)
    print("INPUT MOVIE")
    print("=" * 60)

    print(f"Title  : {input_movie['title']}")
    print(f"Genre  : {input_movie['genres']}")
    print(f"Rating : {input_movie['vote_average']}")

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    print("\n" + "=" * 60)
    print("TOP 5 RECOMMENDATIONS")
    print("=" * 60)

    for rank, movie_data in enumerate(
        movie_list,
        start=1
    ):

        index = movie_data[0]
        score = movie_data[1] * 100

        movie = df.iloc[index]

        print(f"\n{rank}. {movie['title']}")
        print(f"   Genre            : {movie['genres']}")
        print(f"   Rating           : {movie['vote_average']:.1f}")
        print(f"   Similarity Score : {score:.2f}%")

    print("\n" + "=" * 60)


while True:

    movie_name = input(
        "\nEnter Movie Name (or 'exit'): "
    )

    if movie_name.lower() == "exit":
        print("\nThank you for using the system.")
        break

    recommend(movie_name)