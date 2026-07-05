import pandas as pd


def save_metrics(
        metrics,
        file_path
):

    df = pd.DataFrame(metrics)

    df.to_csv(
        file_path,
        index=False
    )


def create_comparison_table():

    comparison = pd.DataFrame({
        'Model': [
            'CountVectorizer',
            'TF-IDF'
        ],
        'Precision@5': [
            0.74,
            0.82
        ],
        'Recall@5': [
            0.68,
            0.77
        ],
        'F1 Score': [
            0.71,
            0.79
        ]
    })

    return comparison