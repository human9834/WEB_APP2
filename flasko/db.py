import sqlite3

DATABASE = 'database.db'

def create_books_table():
    con = sqlite3.connect(DATABASE) # コネクトオブジェクトを作り、データベースにアクセスする
    con.execute("CREATE TABLE IF NOT EXISTS books (title, price, arrival_day)") #table作成SQL
    con.close()


# IF NOT EXISTSで既にあるbooksテーブルと被ってもエラーにならないようになる