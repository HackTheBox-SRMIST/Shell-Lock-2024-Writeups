import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    chat TEXT NOT NULL
)
''')

# Insert sample users with cleaned chat messages
cursor.execute("INSERT INTO users (username, email, password, chat) VALUES ('Rick', 'rickyy@example.com', 'password123', 'Rick: Morty Looks like there is something interesting on your page!')")
cursor.execute("INSERT INTO users (username, email, password, chat) VALUES ('Morty', 'morty@example.com', 'lolpassword', 'Morty: I have a bad feeling about the admin login. Something is off!')")
cursor.execute("INSERT INTO users (username, email, password, chat) VALUES ('Berth', 'berth@example.com', 'securepassword', 'Berth: Maybe we should check the admin_login, guys!')")

# Insert admin user (hidden password)
cursor.execute("INSERT INTO users (username, email, password, chat) VALUES ('admin', 'admin@example.com', 'goddamnityougotit', 'Admin: You wont figure it out that easily!')")

conn.commit()
conn.close()

print("Database setup complete!")
