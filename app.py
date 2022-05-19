from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import mysql.connector
import json
import regex
import database

app = Flask(__name__)

@app.route('/')
def form():
  return render_template("form.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
  name = request.form["name"]
  email = request.form["email"]
    
  if(regex.checkEmail(email)):
    database.db_init()
    database.insertIntoDatabase(name, email)
    
    return render_template("success.html")
  else:
    return render_template("fail.html")


@app.route('/view')
def viewDatabase():
  data = database.view()
  return render_template("view.html", data = data)



if __name__ == "__main__":
  app.run(host ='0.0.0.0')