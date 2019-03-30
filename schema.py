import sqlite3

connect = sqlite3.connect('data.db')
cursor = connect.cursor()

query = "create table if not exists users(id text,firstname text,lastname text,email text,password text)"

try:
    cursor.execute(query)
    print("Table Created")
except Exception as err:
    print(err)
