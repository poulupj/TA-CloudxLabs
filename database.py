import mysql.connector
import json
from mysql_config import app
from mysql_config import mysql
import cryptography

def db_init():
  mydb = mysql.connect()
  cursor = mydb.cursor()

  cursor.execute("CREATE DATABASE IF NOT EXISTS webapp;")
  cursor.close()

  mydb = mysql.connect()
  cursor = mydb.cursor()

  cursor.execute("USE webapp;")
  cursor.execute("CREATE TABLE IF NOT EXISTS info (name VARCHAR(255), email VARCHAR(255), PRIMARY KEY(email));")
  cursor.close()
  mydb.close()
  return 'initialized database'

def insertIntoDatabase(name, email):
  mydb = mysql.connect()
  
  cursor = mydb.cursor()
  cursor.execute("USE webapp;")

  statement = "INSERT INTO info (name, email) VALUES(%s, %s)"
  values = (name, email)

  cursor.execute(statement, values)
  mydb.commit()
  cursor.close()
  mydb.close()

def view():
  mydb = mysql.connect()
  cursor = mydb.cursor()
  cursor.execute("USE webapp;")

  cursor.execute("SELECT * FROM info")

  results = cursor.fetchall()

  cursor.close()
  mydb.close()

  return results