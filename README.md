# MOVIE-RECOMMENDATION-SYSTEM
A software application that suggests content/movies to user based on their prefrences.
This recommendation system follows 'content based filtering approach'. 

# Challeges
Cold start problem, Scalability

# Project Flow
DATASET --> DATA PREPROCESSING --> ML MODEL --> WEBSITE

# DataSet
The system is trained on 'TMDB 5000 Movie Dataset' from Kaggle. Before staring to work on the project, download the dataset.
--DATASET DOWNLOAD LINK--
'https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata'

# Data Preprocessing
Libraries used- 
NUMPY: Array processing package
PANDAS: Data manipulation & analysis
-Creating dataframe, Combinig the two datasets, Creating tags, Checking and removing missing values & duplicate data, Changing format of data-

# ML Model
TEXT VECTORIZATION: Process of converting text data into numerical vector that are used by machine learning algorithms.
Technique used- BAG OF WORDS (BoW): represents text by counting occurences of each word, creating frequency based vector. Lacks contextual understanding
Library- SCIKIT-LEARN (sklearn.feature_extraction.text, CountVectorizer(), fit_transform()), NLTK (PorterStemmer())
important factor- cosine_similarity
pickle module: to convert objects into byte stream and store them in a file, pickle.dump()

# Website
Library- Streamlit
pickle.load()- unpickle to restore original objects
add button and selectbox, including title.
