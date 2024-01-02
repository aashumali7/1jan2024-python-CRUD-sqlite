import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                age INTEGER
            );
        '''
        self.cursor.execute(query)
        self.connection.commit()

    def clear_data(self):
        query = 'DELETE FROM users;'
        self.cursor.execute(query)
        self.connection.commit()

    def insert_data(self, name, surname, age):
        query = 'INSERT INTO users (name, surname, age) VALUES (?, ?, ?);'
        self.cursor.execute(query, (name, surname, age))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

# Example usage
if __name__ == '__main__':
    db_manager = DatabaseManager("./mydb.sqlite")

    # Clear all data in the table
    db_manager.clear_data()

    # Insert new data
    db_manager.insert_data("aashish", "mali", 19)
    db_manager.insert_data("rohit", "mali", 24)

    # Close the connection
    db_manager.close_connection()
