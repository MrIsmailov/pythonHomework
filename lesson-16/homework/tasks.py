import sqlite3
import pandas as pd

# Part 1: Reading Files

# 1. chinook.db
conn = sqlite3.connect('chinook.db')
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print("First 10 rows of customers table:")
print(customers_df.head(10))

# 2. iris.json
iris_df = pd.read_json('iris.json')
print("\nShape of iris dataset:", iris_df.shape)
print("Column names of iris dataset:", iris_df.columns)

# 3. titanic.xlsx
titanic_df = pd.read_excel('titanic.xlsx')
print("\nFirst 5 rows of titanic dataset:")
print(titanic_df.head())

# 4. Flights parquet file
flights_df = pd.read_parquet('flights.parquet')
print("\nSummary of flights dataset:")
print(flights_df.info())

# 5. movie.csv
movie_df = pd.read_csv('movie.csv')
print("\nRandom sample of 10 rows from movie dataset:")
print(movie_df.sample(10))

# Part 2: Exploring DataFrames

# Using the DataFrame from iris.json
# Rename the columns to lowercase
iris_df.columns = iris_df.columns.str.lower()
print("\nColumns after renaming to lowercase:", iris_df.columns)

# Select only the sepal_length and sepal_width columns
iris_selected_df = iris_df[['sepal_length', 'sepal_width']]
print("\nSelected columns from iris dataset:")
print(iris_selected_df.head())

# From the titanic.xlsx DataFrame
# Filter rows where the age of passengers is above 30
titanic_filtered_df = titanic_df[titanic_df['Age'] > 30]
print("\nPassengers with age above 30:")
print(titanic_filtered_df.head())

# Count the number of male and female passengers (value_counts)
gender_counts = titanic_df['Sex'].value_counts()
print("\nNumber of male and female passengers:")
print(gender_counts)

# From the Flights parquet file
# Extract and print only the origin, dest, and carrier columns
flights_selected_df = flights_df[['origin', 'dest', 'carrier']]
print("\nSelected columns from flights dataset:")
print(flights_selected_df.head())

# Find the number of unique destinations
unique_destinations = flights_df['dest'].nunique()
print("\nNumber of unique destinations:", unique_destinations)

# From the movie.csv file
# Filter rows where duration is greater than 120 minutes
long_movies_df = movie_df[movie_df['duration'] > 120]
print("\nMovies with duration greater than 120 minutes:")
print(long_movies_df.head())

# Sort the filtered DataFrame by director_facebook_likes in descending order
sorted_long_movies_df = long_movies_df.sort_values(by='director_facebook_likes', ascending=False)
print("\nSorted movies by director_facebook_likes:")
print(sorted_long_movies_df.head())

# Part 3: Challenges and Explorations

# From iris.json: Calculate the mean, median, and standard deviation for each numerical column
iris_stats = iris_df.describe().loc[['mean', '50%', 'std']]
iris_stats.rename(index={'50%': 'median'}, inplace=True)
print("\nMean, median, and standard deviation for each numerical column in iris dataset:")
print(iris_stats)

# From titanic.xlsx: Find the minimum, maximum, and sum of passenger ages
age_stats = titanic_df['Age'].agg(['min', 'max', 'sum'])
print("\nMinimum, maximum, and sum of passenger ages in titanic dataset:")
print(age_stats)

# From movie.csv
# Identify the director with the highest total director_facebook_likes
director_likes = movie_df.groupby('director_name')['director_facebook_likes'].sum().idxmax()
print("\nDirector with the highest total director_facebook_likes:", director_likes)

# Find the 5 longest movies and their respective directors
longest_movies = movie_df.nlargest(5, 'duration')[['title', 'director_name', 'duration']]
print("\n5 longest movies and their respective directors:")
print(longest_movies)

# From Flights parquet file
# Check for missing values in the dataset
missing_values = flights_df.isnull().sum()
print("\nMissing values in flights dataset:")
print(missing_values)

# Fill missing values in a numerical column with the column’s mean
flights_df['dep_delay'].fillna(flights_df['dep_delay'].mean(), inplace=True)
print("\nMissing values in 'dep_delay' column after filling with mean:")
print(flights_df['dep_delay'].isnull().sum())