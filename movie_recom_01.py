

# 1. Import libraries
import pandas as pd
import numpy as np
import difflib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# 2. Load dataset
movies_data = pd.read_csv("movies.csv")

# Remove rows without movie titles
movies_data = movies_data.dropna(subset=["title"]).reset_index(drop=True)


# 3. Select important features
selected_features = [
    "genres",
    "keywords",
    "tagline",
    "cast",
    "director"
]


# 4. Handle missing values
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna("").astype(str)


# 5. Combine movie features
combined_features = (
    movies_data[selected_features]
    .agg(" ".join, axis=1)
)


# 6. Convert text into memory-efficient vectors
vectorizer = TfidfVectorizer(
    dtype=np.float32,
    sublinear_tf=True
)

feature_vectors = vectorizer.fit_transform(combined_features)

print("Movie dataset loaded successfully!")
print(f"Total movies: {len(movies_data)}")


# 7. Get movie name from user
movie_name = input("\nEnter your favourite movie name: ").strip()

if not movie_name:
    print("Please enter a movie name.")

else:
    # 8. Find the closest movie title
    all_titles = movies_data["title"].tolist()

    matches = difflib.get_close_matches(
        movie_name,
        all_titles,
        n=1,
        cutoff=0.4
    )

    if not matches:
        print("Movie not found. Please try another movie name.")

    else:
        close_match = matches[0]

        # 9. Find the selected movie index
        movie_index = movies_data.index[
            movies_data["title"] == close_match
        ][0]

        # 10. Calculate similarity ONLY for the selected movie
        similarity_scores = cosine_similarity(
            feature_vectors[movie_index],
            feature_vectors,
            dense_output=False
        ).toarray().ravel()

        # 11. Select the top 11 candidates efficiently
        top_n = min(11, len(movies_data))

        top_indices = np.argpartition(
            similarity_scores,
            -top_n
        )[-top_n:]

        # Sort selected candidates by similarity
        top_indices = top_indices[
            np.argsort(similarity_scores[top_indices])[::-1]
        ]

        print(f"\nMovies similar to {close_match}:\n")

        # 12. Display up to 10 recommendations
        count = 0

        for index in top_indices:

            # Skip the selected movie
            if index == movie_index:
                continue

            movie = movies_data.iloc[index]
            score = similarity_scores[index]

            print(f"{count + 1}. Movie Name: {movie['title']}")
            print(f"   Language: {movie.get('original_language', 'N/A')}")
            print(f"   Similarity Score: {score:.2f}")
            print(f"   Genre: {movie.get('genres', 'N/A')}")
            print(f"   Popularity: {movie.get('popularity', 'N/A')}")
            print(f"   Release Date: {movie.get('release_date', 'N/A')}")
            print(f"   Homepage: {movie.get('homepage', 'N/A')}")
            print(f"   Overview: {movie.get('overview', 'N/A')}")
            print("-" * 50)

            count += 1

            if count == 10:
                break
