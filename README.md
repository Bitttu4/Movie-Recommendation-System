# Movie Recommendation System using Machine Learning

A machine learning-based movie recommendation system that recommends similar movies using content-based filtering techniques and compares the performance of two recommendation approaches.

---

## Project Overview

This project recommends movies based on their metadata, including:

- Genres
- Keywords
- Cast
- Director
- Movie Overview

The system implements and compares two recommendation models:

1. CountVectorizer + Cosine Similarity
2. TF-IDF + Cosine Similarity

The project also performs exploratory data analysis, generates visualizations, and automatically saves evaluation metrics and recommendation outputs.

---

## Features

- Content-Based Movie Recommendation System
- Two Recommendation Models
- Exploratory Data Analysis (EDA)
- Automatic Visualization Generation
- Automatic CSV Export
- Similarity Matrix Visualization
- Model Comparison
- Execution Time Comparison
- Professional Notebook Structure
- Modular Project Structure

---

## Project Structure

```text
Movie-Recommendation-System/
│
├── datasets/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── images/
│
├── notebooks/
│   └── Movie_Recommendation_System.ipynb
│
├── outputs/
│   ├── metrics/
│   │   ├── execution_time.csv
│   │   └── model_comparison.csv
│   │
│   ├── recommendations/
│   │   └── avatar_recommendations.csv
│   │
│   └── processed_movies.csv
│
├── src/
│   ├── preprocessing.py
│   ├── model_countvectorizer.py
│   ├── model_tfidf.py
│   ├── recommender.py
│   └── evaluation.py
│
├── requirements.txt
├── run.py
├── README.md
└── LICENSE
```

---

## Dataset

Dataset Used:

TMDB 5000 Movie Dataset

Dataset Files:

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

The dataset contains information related to:

- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Popularity
- Ratings
- Release Date
- Overview

---

## Technologies Used

### Programming Language

- Python

### Libraries

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- NLTK
- Plotly
- Jupyter Notebook

---

## Models Implemented

### Model 1

CountVectorizer + Cosine Similarity

Advantages:

- Fast
- Simple
- Computationally Efficient

---

### Model 2

TF-IDF + Cosine Similarity

Advantages:

- Better Recommendation Quality
- Reduces Impact of Common Words
- Gives Higher Importance to Meaningful Features

---

## Evaluation Metrics

- Precision@5
- Recall@5
- F1 Score
- Execution Time

> Note:
> Exact evaluation of recommendation systems generally requires user interaction data or rating datasets. The evaluation metrics used in this project are comparative demonstration metrics.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Bitttu4/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

---

### Create Virtual Environment (Optional)

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Use

### Option 1: Using Jupyter Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/Movie_Recommendation_System.ipynb
```

The notebook performs the following tasks:

1. Loads the TMDB datasets.
2. Performs exploratory data analysis.
3. Cleans and preprocesses the data.
4. Extracts genres, keywords, cast, and director information.
5. Creates movie tags.
6. Builds two recommendation models.
7. Generates movie recommendations.
8. Creates visualizations and heatmaps.
9. Saves generated CSV files and plots.

---

### Option 2: Using Python Script

Execute:

```bash
python run.py
```

The script will:

1. Load the datasets.
2. Preprocess the movie data.
3. Build recommendation models.
4. Generate similarity matrices.
5. Generate recommendations.
6. Save processed datasets.
7. Save recommendation outputs.
8. Save evaluation metrics.
9. Save all visualizations and graphs.

Generated files will be stored in:

```text
images/
outputs/
```

---

## Example Usage

```python
recommend_cv("Avatar")

recommend_tfidf("Avatar")
```

---

## Sample Recommendation

### Input

```text
Avatar
```

### Output

```text
Aliens
Falcon Rising
Battle: Los Angeles
Aliens vs Predator: Requiem
Apollo 18
```

---

## Generated Outputs

### CSV Files

```text
outputs/
├── processed_movies.csv
├── recommendations/avatar_recommendations.csv
├── metrics/model_comparison.csv
└── metrics/execution_time.csv
```

---

### Generated Visualizations

```text
images/
├── missing_values_heatmap.png
├── correlation_heatmap.png
├── popularity_distribution.png
├── vote_average_distribution.png
├── similarity_heatmap_countvectorizer.png
├── similarity_heatmap_tfidf.png
├── precision_comparison.png
├── recall_comparison.png
├── f1_comparison.png
└── execution_time_comparison.png
```

---

## Future Scope

- Collaborative Filtering
- Hybrid Recommendation Systems
- Real-Time Movie APIs
- Streamlit Web Application
- Personalized Recommendations using User Ratings
- Deep Learning-Based Recommendation Systems

---

## Conclusion

Both recommendation models successfully generate meaningful movie recommendations.

CountVectorizer provides a simple and computationally efficient baseline approach, while TF-IDF produces more refined recommendations by assigning greater importance to meaningful terms.

Based on comparative analysis, the TF-IDF model provides better recommendation quality for this dataset.

---

## Author

Aarya Patel

GitHub: <https://github.com/Bitttu4>

---

## License

This project is licensed under the MIT License.
