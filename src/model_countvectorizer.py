from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_countvectorizer_model(df):

    cv = CountVectorizer(
        max_features=5000,
        stop_words='english'
    )

    vectors = cv.fit_transform(
        df['tags']
    ).toarray()

    similarity = cosine_similarity(vectors)

    return cv, similarity


def recommend_cv(df, similarity, movie):

    movie = movie.lower()

    matches = df[
        df['title'].str.lower() == movie
    ]

    if matches.empty:
        return []

    movie_index = matches.index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        recommendations.append(
            df.iloc[i[0]].title
        )

    return recommendations