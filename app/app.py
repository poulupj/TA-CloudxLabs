from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def form():
  return render_template("form.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
    name = request.form["name"]
    email = request.form["email"]
    
    return "success"


if __name__ == "__main__":
  app.run(host ='0.0.0.0')