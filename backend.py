import sqlite3

class Database:

    #init function always start when class object is called - it's like the constructor
    #when we call a method of class, the class is sending object instance to this method as well, that's why one of the arguments should be 'self'
    #most of the previous local variables should be now atributes so the object can use it with every method (e.g. self.cur ...)
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER )")


    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))  #NULL stands for id primary key, python deals with it itself giving the next available id
        self.conn.commit()
       

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""): #adding empty strings to enable passing just one parameter into function (just passing e.g. author will return the whole row)
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):  #we expect to have id of the row which will be deleted, id will be extraced from the tuple
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()
    

    def update(self,id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.conn.commit()
    
    #method which is executed when an instance of the class closed ( in our case when the script closes )
    #in our case this method closes connection with database
    def __del__(self):
        self.conn.close()

   

