import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS boo(login, password)")


def add(user):
	cursor.execute("INSERT INTO  boo VALUES(?, ?)", user)
	conn.commit()

add((input("login: "), input("password: ")))
