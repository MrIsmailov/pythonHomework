import sqlite3
import pandas as pd

# Part 1: Merging and Joining

# Inner Join on Chinook Database
conn = sqlite3.connect('chinook.db')
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
invoices_df = pd.read_sql_query("SELECT * FROM invoices", conn)

# Perform an inner join between the customers and invoices tables on the CustomerId column
merged_df = pd.merge(customers_df, invoices_df, on='CustomerId', how='inner')

# Find the total number of invoices for each customer
invoice_counts = merged_df.groupby('CustomerId').size()
print("Total number of invoices for each customer:")
print(invoice_counts)

# Outer Join on Movie Data
movie_df = pd.read_csv('movie.csv')

# Create two smaller DataFrames
df1 = movie_df[['director_name', 'color']]
df2 = movie_df[['director_name', 'num_critic_for_reviews']]

# Perform a left join and then a full outer join on director_name
left_join_df = pd.merge(df1, df2, on='director_name', how='left')
outer_join_df = pd.merge(df1, df2, on='director_name', how='outer')

# Count how many rows are in the resulting DataFrames for each join type
print("\nNumber of rows in left join DataFrame:", len(left_join_df))
print("Number of rows in full outer join DataFrame:", len(outer_join_df))

# Part 2: Grouping and Aggregating

# Grouped Aggregations on Titanic
titanic_df = pd.read_excel('titanic.xlsx')

# Group passengers by Pclass and calculate the average age, total fare, and count of passengers
grouped_titanic_df = titanic_df.groupby('Pclass').agg({
    'Age': 'mean',
    'Fare': 'sum',
    'PassengerId': 'count'
}).rename(columns={'PassengerId': 'PassengerCount'})
print("\nGrouped aggregations on Titanic dataset:")
print(grouped_titanic_df)

# Multi-level Grouping on Movie Data
# Group the movies by color and director_name
grouped_movie_df = movie_df.groupby(['color', 'director_name']).agg({
    'num_critic_for_reviews': 'sum',
    'duration': 'mean'
})
print("\nMulti-level grouping on Movie dataset:")
print(grouped_movie_df)

# Nested Grouping on Flights
flights_df = pd.read_parquet('flights.parquet')

# Group flights by Year and Month and calculate total number of flights, average arrival delay, and maximum departure delay
grouped_flights_df = flights_df.groupby(['Year', 'Month']).agg({
    'FlightNum': 'count',
    'ArrDelay': 'mean',
    'DepDelay': 'max'
}).rename(columns={'FlightNum': 'TotalFlights'})
print("\nNested grouping on Flights dataset:")
print(grouped_flights_df)

# Part 3: Applying Functions

# Apply a Custom Function on Titanic
def classify_age(age):
    return 'Child' if age < 18 else 'Adult'

titanic_df['Age_Group'] = titanic_df['Age'].apply(classify_age)
print("\nTitanic dataset with Age_Group column:")
print(titanic_df[['Age', 'Age_Group']].head())

# Normalize Employee Salaries
employee_df = pd.read_csv('employee.csv')

# Normalize the salaries within each department
employee_df['NormalizedSalary'] = employee_df.groupby('Department')['Salary'].transform(lambda x: (x - x.mean()) / x.std())
print("\nEmployee dataset with NormalizedSalary column:")
print(employee_df[['Department', 'Salary', 'NormalizedSalary']].head())

# Custom Function on Movies
def classify_duration(duration):
    if duration < 60:
        return 'Short'
    elif duration <= 120:
        return 'Medium'
    else:
        return 'Long'

movie_df['Duration_Category'] = movie_df['duration'].apply(classify_duration)
print("\nMovie dataset with Duration_Category column:")
print(movie_df[['duration', 'Duration_Category']].head())

# Part 4: Using pipe

# Pipeline on Titanic
def filter_survived(df):
    return df[df['Survived'] == 1]

def fill_missing_age(df):
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    return df

def create_fare_per_age(df):
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df

titanic_pipeline_df = (titanic_df.pipe(filter_survived)
                       .pipe(fill_missing_age)
                       .pipe(create_fare_per_age))
print("\nTitanic dataset after pipeline:")
print(titanic_pipeline_df.head())

# Pipeline on Flights
def filter_delayed_flights(df):
    return df[df['DepDelay'] > 30]

def add_delay_per_hour(df):
    df['Delay_Per_Hour'] = df['DepDelay'] / df['AirTime']
    return df

flights_pipeline_df = (flights_df.pipe(filter_delayed_flights)
                       .pipe(add_delay_per_hour))
print("\nFlights dataset after pipeline:")
print(flights_pipeline_df.head())