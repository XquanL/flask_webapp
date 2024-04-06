from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'xl395'

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods = ['POST','GET'])
def greet():
    flash("Hi " + str(request.form['name_input'] + ", greet to see you!" + "\n YOU'RE THE BEST!"))
    return render_template("index.html")
    
