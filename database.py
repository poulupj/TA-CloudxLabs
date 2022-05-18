import mysql.connector
import json

def db_init():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1"
  )
  cursor = mydb.cursor()

  cursor.execute("CREATE DATABASE IF NOT EXISTS webapp;")
  cursor.close()

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="webapp"
  )
  cursor = mydb.cursor()

  cursor.execute("CREATE TABLE IF NOT EXISTS info (name VARCHAR(255), email VARCHAR(255));")
  cursor.close()

  return 'initialized database'

def insertIntoDatabase(name, email):
  mydb = mysql.connector.connect(
      host="mysqldb",
      user="root",
      password="p@ssw0rd1",
      database="webapp"
  )
  
  cursor = mydb.cursor()

  statement = "INSERT INTO info (name, email) VALUES(%s, %s)"
  values = (name, email)

  cursor.execute(statement, values)
  mydb.commit()
  cursor.close()

def view():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="webapp"
  )
  cursor = mydb.cursor()


  cursor.execute("SELECT * FROM info")

  row_headers=[x[0] for x in cursor.description] #this will extract row headers

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)