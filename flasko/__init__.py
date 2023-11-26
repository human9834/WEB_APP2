from flask import Flask
app = Flask(__name__)
import flasko.main

# dbの呼び出し
from flasko import db
db.create_books_table()

