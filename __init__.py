import sqlite3

conn = sqlite3.connect('locker_data.db')

c = conn.cursor()

def locker_searcher():
    data = search()
    display(data)
    
def search():
    teacher = input("Enter Teacher Name: ")
    test = 'SELECT name,locker FROM locker_data WHERE name LIKE "%{}%"'.format(teacher)
    data = c.execute(test)
    return data

def display(data):
    for name, locker in data:
        print("Name: {0}, Locker: {1}".format(name,locker))
        
#------------------------------------Above is the python code for accessing the database------------------------------------#

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
