from flask import Flask
from flaskext.mysql import MySQL
import cryptography

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'p@ssw0rd1'
app.config['MYSQL_DATABASE_HOST'] = 'mysqldb'


mysql = MySQL(app)