import pandas as pd


def save_recommendations(
        recommendations,
        file_path
):

    df = pd.DataFrame(
        recommendations,
        columns=['Recommendations']
    )

    df.to_csv(
        file_path,
        index=False
    )


def print_recommendations(
        recommendations
):

    for i, movie in enumerate(
            recommendations,
            start=1
    ):
        print(f"{i}. {movie}")