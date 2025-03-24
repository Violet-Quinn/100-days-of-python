import sqlite3,flask,sqlalchemy,flask_sqlalchemy
db=sqlite3.connect('books-collection.db')
cursor=db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,"
#                " title varchar(250) NOT NULL UNIQUE,"
#                " author varchar(250) NOT NULL,"
#                " rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1,'Harry Potter','J.K. Rowling','7.1')")
# db.commit()

