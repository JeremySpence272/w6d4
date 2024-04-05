import sqlite3

# Set up a SQLite database using Python's SQLite3 module.
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# First, create the user_profiles table.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age INTEGER,
        gender TEXT,
        address TEXT
    )
''')

# Then, create the user_accounts table with a foreign key referencing user_profiles.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        password TEXT,
        profile INTEGER,
        FOREIGN KEY (profile) REFERENCES user_profiles (id)
    )
''')

conn.commit()
conn.close()
