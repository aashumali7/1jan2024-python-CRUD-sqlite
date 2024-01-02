import sqlite3
import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

def submitForm(): #camelCase
    print("hello")
    name = name_edit.text()
    surname = surname_edit.text()
    age = age_edit.text()


    # Perform further actions with the captured data
    # For example, insert data into the database
    cursor.execute('INSERT INTO users (name, surname, age) VALUES (?, ?, ?)', (name, surname, age))
    con.commit()

    # Clear the input fields
    name_edit.clear()
    surname_edit.clear()
    age_edit.clear()

    # Show a popup message
    QMessageBox.information(main_window, 'Registration Successful', 'User information has been successfully registered.')


app = QApplication([]) #[] empty list passing

# Create widgets
name_label = QLabel('Name:')
name_edit = QLineEdit()

surname_label = QLabel('Surname:')
surname_edit = QLineEdit()

age_label = QLabel('Age:')
age_edit = QLineEdit()

submit_button = QPushButton('Submit')
submit_button.clicked.connect(submitForm)#calling the function
# Set button color to blue
submit_button.setStyleSheet("background-color: blue; color: white;")

# Layout
layout = QVBoxLayout()

layout.addWidget(name_label)
layout.addWidget(name_edit)

layout.addWidget(surname_label)
layout.addWidget(surname_edit)

layout.addWidget(age_label)
layout.addWidget(age_edit)

layout.addWidget(submit_button)

# Create the main window
main_window = QMainWindow()
main_window.setWindowTitle('User Information Form')
#main_window.setGeometry(X,  Y,   W,     H)
main_window.setGeometry(10, 50, 300, 200)

# Database connection
con = sqlite3.connect("./mydb.sqlite")
cursor = con.cursor()

# Create the 'users' table if not exists
query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        age INTEGER
    );
'''
cursor.execute(query)
con.commit()

# Clear all data in the table
query = 'DELETE FROM users;'
cursor.execute(query)
con.commit()

# Set up the layout in the main window
central_widget = QWidget()
central_widget.setLayout(layout)
main_window.setCentralWidget(central_widget)

# Show the main window
main_window.show()
sys.exit(app.exec())
