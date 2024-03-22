# It will not be used in the final project
# It is just for testing purposes

import sqlite3

# Schema name
SCHEMA_NAME = 'myapi'

# Connect to SQLite database (creates the database file if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Define the SQL command to create a table
create_table_sql = """
CREATE TABLE simple_item (
    id INTEGER PRIMARY KEY,
    text TEXT NOT NULL,
    count INTEGER NOT NULL
)
"""

# Execute the SQL command to create the table
cur.execute(create_table_sql)

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
