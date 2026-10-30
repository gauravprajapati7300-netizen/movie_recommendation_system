# 🎬 Movie Recommendation System

## 📌 Project Overview

The **Movie Recommendation System** is a Python-based machine learning project that recommends movies to users based on the movie they like.

It analyzes movie information such as genres, keywords, overview, cast, director, and tagline to identify similar movies. It uses **TF-IDF Vectorization** and **Cosine Similarity** to calculate how closely movies are related.

The main goal of this project is to help users discover movies according to their interests.

## 🎯 Objectives

- Recommend movies similar to a user's favorite movie.
- Analyze movie details to find similarities.
- Apply machine learning and natural language processing techniques.
- Provide relevant recommendations efficiently.
- Learn how recommendation systems work in real-world applications.

## 🛠️ Technologies Used

- **Python** – Main programming language
- **Pandas** – Data loading and data processing
- **NumPy** – Numerical operations
- **Scikit-learn** – TF-IDF vectorization and cosine similarity
- **Difflib** – Finding similar movie titles when the entered name is not exact
- **Jupyter Notebook** – Developing and testing the project

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── movies.csv
├── movie_recommendation.ipynb
├── movie_recom_documentation.py
├── README.md
└── Movie_Recommendation_System_Documentation.docx
```

*Note: Update the filenames above if your actual project files have different names.*

## ⚙️ How It Works

1. **Load the Dataset:** The system reads movie information from `movies.csv`.
2. **Select Features:** Important information such as genres, keywords, overview, cast, director, and tagline is selected.
3. **Combine Text Features:** Selected information is combined to create a text representation of each movie.
4. **TF-IDF Vectorization:** Text data is converted into numerical vectors that the computer can process.
5. **Cosine Similarity:** The system calculates similarity scores between movies.
6. **Find the Movie:** The system searches for the movie entered by the user. If the title is not an exact match, it can suggest a similar title.
7. **Recommend Movies:** The system displays movies that are most similar to the selected movie.

## 📦 Installation

Make sure Python is installed on your computer.

Install the required libraries using:

```bash
python -m pip install pandas numpy scikit-learn
```

If you want to run the project in Jupyter Notebook, install Jupyter as well:

```bash
python -m pip install notebook
```

## ▶️ How to Run the Project

### Using Jupyter Notebook

1. Open the project folder.
2. Open PowerShell or Command Prompt in that folder.
3. Run:

```bash
jupyter notebook
```

4. Open your movie recommendation notebook.
5. Run the cells in order.
6. Enter a movie title when prompted to get recommendations.

### Using a Python Script

If you have converted the notebook into a Python file, run:

```bash
python movie_recommendation.py
```

Make sure the dataset file `movies.csv` is available in the expected location.

## 💡 Example

**Input:**
```text
Enter your favourite movie: Avatar
```

**Output:**
```text
Movies suggested for you:

1. Guardians of the Galaxy
2. Star Trek
3. John Carter
4. The Avengers
5. Man of Steel
```

*These are illustrative examples. Actual recommendations depend on the dataset and the similarity scores calculated by your program.*

## 🚀 Features

- Content-based movie recommendations
- Movie similarity calculation
- Automatic matching of similar movie titles
- Uses multiple movie attributes for recommendations
- Efficient similarity processing
- Easy-to-understand Python implementation

## 📊 Machine Learning Concepts

### 1. TF-IDF Vectorization

TF-IDF stands for **Term Frequency–Inverse Document Frequency**. It converts text into numerical values and helps identify important words in movie information.

### 2. Cosine Similarity

Cosine similarity measures how similar two numerical vectors are. A higher similarity score generally indicates that two movies have more similar content features.

### 3. Content-Based Filtering

Content-based filtering recommends items based on their characteristics. In this project, movies are recommended by comparing their information rather than relying on other users' ratings or preferences.

## 🔮 Future Improvements

- Develop a web interface using Flask or Django.
- Add movie posters and detailed movie information.
- Include user ratings and personalized preferences.
- Connect to a movie information API.
- Improve recommendations using collaborative filtering.
- Deploy the project online for public use.

## 🎓 Learning Outcomes

Through this project, I learned about:

- Data processing with Pandas and NumPy
- Text preprocessing and feature selection
- TF-IDF vectorization
- Cosine similarity
- Content-based recommendation systems
- Building a practical machine learning project using Python

## 👨‍💻 Author

**Gaurav Prajapati**

B.Tech Student  
Bharat Institute of Technology (BIT)

## 📄 License

This project was developed for educational and learning purposes. If you redistribute the project or dataset, follow the applicable license and usage terms.

---

⭐ **If you find this project useful, consider giving it a star on GitHub!**
