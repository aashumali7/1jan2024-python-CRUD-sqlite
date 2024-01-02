#import area
import sqlite3
  
  # = module.method()
con = sqlite3.connect("./mydb.sqlite")
cursor = con.cursor()

query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                age INTEGER
            );
        '''
cursor.execute(query) #query is a actual argument
con.commit()

# Clear all data in the table
query = 'DELETE FROM users;'
cursor.execute(query)

query = 'INSERT INTO users (name, surname, age) VALUES (?, ?, ?);'
cursor.execute(query, ("aashish", "mali", 19))
cursor.execute(query, ("rohit", "mali", 24))
con.commit()
