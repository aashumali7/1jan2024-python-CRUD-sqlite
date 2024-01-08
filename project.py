from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QTableWidgetItem, QHBoxLayout
import sqlite3
import sys

def submitForm():
    print("hello")
    name = name_edit.text()
    surname = surname_edit.text()
    age = age_edit.text()

    cursor.execute('INSERT INTO users (name, surname, age) VALUES (?, ?, ?)', (name, surname, age))
    con.commit()

    name_edit.clear()
    surname_edit.clear()
    age_edit.clear()

    QMessageBox.information(main_window, 'Registration Successful', 'User information has been successfully registered.')

def deleteUsers(row):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Question)
    msg_box.setText('Do you want to Delete?')
    msg_box.setWindowTitle('Confirmation')
    msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    msg_box.setDefaultButton(QMessageBox.StandardButton.No)

    result = msg_box.exec()

    if result == QMessageBox.StandardButton.Yes:
        print('Yes button clicked')
        # Add your code for "Yes" action here
        print(table.item(row,0).text())
        delid = table.item(row,0).text()
        print(type(delid))
        # typecasting
        delid = int(delid)
        print(f'DELETE FROM users WHERE id ={delid}')
        cursor.execute(f"DELETE FROM users WHERE id ={delid}")

        cursor.execute(query)
        con.commit()
        # Clear the table
        table.clear()
        table.removeRow(row)
        # Call showDetails to reload updated data
        showDetails(row)

    else:
        print('No button clicked or closed')
        # Add your code for "No" action here

def editUser(row):
    QMessageBox.information(main_window, 'View User', f'Viewing details for user with ID: {table.item(row, 0).text()}')

# ...
def showDetails(row):
    print('hey')
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    columns_name = ['ID', "Name", "Surname", 'Age', "Actions"]
    table.setColumnCount(len(columns_name))
    table.setHorizontalHeaderLabels(columns_name)

    table.setRowCount(len(data))
    for row_num, row_data in enumerate(data):
        delid = ''
        for col_num, col_data in enumerate(row_data):
            item = QTableWidgetItem(str(col_data))
            table.setItem(row_num, col_num, item)
            if col_num == 0:
                print(f'col data >> {col_data}')
                delid = col_data
                pass

        delete_button = QPushButton('Delete')
        edit_button = QPushButton('Edit')
        button_layout = QHBoxLayout()
        button_layout.addWidget(delete_button)
        button_layout.addWidget(edit_button)
        button_layout.setContentsMargins(0, 0, 0, 0)

        delete_button.clicked.connect(lambda _, row=row_num: deleteUsers(row))
        edit_button.clicked.connect(lambda _, row=row_num: editUser(row))  # Connect to the editUser function

        # Create a container widget and set the layout to it
        container_widget = QWidget()
        container_widget.setLayout(button_layout)
       
        # Set the background color of the delete button to red
        delete_button.setStyleSheet("background-color: red; color: white;")
        edit_button.setStyleSheet("background-color: purple; color: white;")

        # Set the container widget as the cell widget
        table.setCellWidget(row_num, len(columns_name) - 1, container_widget)

    table.show()
    print(data)


app = QApplication([])

name_label = QLabel('Name:')
name_edit = QLineEdit()

surname_label = QLabel('Surname:')
surname_edit = QLineEdit()

age_label = QLabel('Age:')
age_edit = QLineEdit()

submit_button = QPushButton('Submit')
submit_button.clicked.connect(submitForm)
submit_button.setStyleSheet("background-color: blue; color: white;")

show_button = QPushButton('Show Details')
show_button.setStyleSheet("background-color: green; color: white;")
show_button.clicked.connect(showDetails)

table = QTableWidget()

layout = QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(name_edit)

layout.addWidget(surname_label)
layout.addWidget(surname_edit)

layout.addWidget(age_label)
layout.addWidget(age_edit)

layout.addWidget(submit_button)
layout.addWidget(show_button)
layout.addWidget(table)

main_window = QMainWindow()
main_window.setWindowTitle('User Information Form')
main_window.setGeometry(10, 50, 600, 400)

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

central_widget = QWidget()
central_widget.setLayout(layout)
main_window.setCentralWidget(central_widget)

main_window.show()
sys.exit(app.exec())
