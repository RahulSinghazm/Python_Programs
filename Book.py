import sqlite3
Book1=sqlite3.connect('Book.db')
curb=Book1.cursor()
curb.execute('''create table Bookname(
bookname varchar,authorname varchar,price float);''')
Book1.close()
