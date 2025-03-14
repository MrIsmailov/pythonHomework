import sqlite3

# Task 1: 
def create_roster_db():
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
    ''')

    roster_data = [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ]
    cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', roster_data)

    cursor.execute('UPDATE Roster SET Name = ? WHERE Name = ?', ('Ezri Dax', 'Jadzia Dax'))

    cursor.execute('SELECT Name, Age FROM Roster WHERE Species = ?', ('Bajoran',))
    bajoran_characters = cursor.fetchall()
    print("Bajoran Characters:")
    for character in bajoran_characters:
        print(character)


    cursor.execute('DELETE FROM Roster WHERE Age > 100')

    # Bonus Task: 
    cursor.execute('PRAGMA table_info(Roster)')
    columns = [info[1] for info in cursor.fetchall()]
    if 'Rank' not in columns:
        cursor.execute('ALTER TABLE Roster ADD COLUMN Rank TEXT')
    rank_data = [
        ('Benjamin Sisko', 'Captain'),
        ('Ezri Dax', 'Lieutenant'),
        ('Kira Nerys', 'Major')
    ]
    for name, rank in rank_data:
        cursor.execute('UPDATE Roster SET Rank = ? WHERE Name = ?', (rank, name))

    cursor.execute('SELECT * FROM Roster ORDER BY Age DESC')
    sorted_characters = cursor.fetchall()
    print("Characters sorted by Age (descending):")
    for character in sorted_characters:
        print(character)

    conn.commit()
    conn.close()

# Task 2: 

def create_library_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
    ''')

    books_data = [
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
        ('1984', 'George Orwell', 1949, 'Dystopian'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
    ]
    cursor.executemany('INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)', books_data)

    cursor.execute('UPDATE Books SET Year_Published = ? WHERE Title = ?', (1950, '1984'))

    cursor.execute('SELECT Title, Author FROM Books WHERE Genre = ?', ('Dystopian',))
    dystopian_books = cursor.fetchall()
    print("Dystopian Books:")
    for book in dystopian_books:
        print(book)

    cursor.execute('DELETE FROM Books WHERE Year_Published < 1950')

    # Bonus Task:
    cursor.execute('PRAGMA table_info(Books)')
    columns = [info[1] for info in cursor.fetchall()]
    if 'Rating' not in columns:
        cursor.execute('ALTER TABLE Books ADD COLUMN Rating REAL')
    rating_data = [
        ('To Kill a Mockingbird', 4.8),
        ('1984', 4.7),
        ('The Great Gatsby', 4.5)
    ]
    for title, rating in rating_data:
        cursor.execute('UPDATE Books SET Rating = ? WHERE Title = ?', (rating, title))

    cursor.execute('SELECT * FROM Books ORDER BY Year_Published ASC')
    sorted_books = cursor.fetchall()
    print("Books sorted by Year Published (ascending):")
    for book in sorted_books:
        print(book)

    conn.commit()
    conn.close()

create_roster_db()
create_library_db()