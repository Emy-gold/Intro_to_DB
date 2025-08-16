import mysql.connector
from mysql.connector import Error 

try :
    mydb = mysql.connector.connect(
        host = "localhost",
        root = "root",
        password = "IMan2004$"
    )

    if(mydb.is_connected):
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store.sql")
        print("Database 'alx_book_store' created successfully!")
