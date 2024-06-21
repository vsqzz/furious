import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create the settings table
c.execute('''
          CREATE TABLE IF NOT EXISTS settings
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          value TEXT NOT NULL)
          ''')

# Insert initial settings
c.execute('''
          INSERT OR IGNORE INTO settings (name, value)
          VALUES
          ('prefix', '!'),
          ('welcome_message', 'Welcome to the server!'),
          ('invite_link', 'https://discord.gg/example')
          ''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database initialized with default settings.")
