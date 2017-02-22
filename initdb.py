import sqlite3

connection = sqlite3.connect('database.db')
print('Opened database successfully')

connection.execute('CREATE TABLE info (name TEXT, language TEXT, country TEXT)')
print('Table created successfully')

connection.close()
