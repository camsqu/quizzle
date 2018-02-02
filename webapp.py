import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.
                                     #The value should be set in Heroku (Settings->Config Vars).

@app.route('/')
def renderMain():
    return render_template('home.html', yourScore = "Score: 0")

@app.route('/startOver')
def startOver():
    #clear variable values and create a new session
    session.clear()
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/quiz', methods=['GET','POST'])
def renderPage1():
    return render_template('home.html', yourScore = "Score: 0")

@app.route('/checkScore', methods=['GET','POST'])
def checkScore():
    #clear variable values and create a new session
    session["q1"] = request.form["q1"]
    session["q2"] = request.form["q2"]
    session["q3"] = request.form["q3"]
    answers = [request.form["q1"], request.form["q2"], request.form["q3"]]
    return render_template('home.html' , yourScore = get_score(answers))
# @app.route('/page2',methods=['GET','POST'])
# def renderPage2():
    #set the first and last name in the session
    # session["firstName"] = request.form["firstName"]
    # session["lastName"] = request.form["lastName"]
    # return render_template('page2.html')

# @app.route('/page3',methods=['GET','POST'])
# def renderPage3():
    #set the favorite color in the session
    # session["favoriteColor"] = request.form["favoriteColor"]
    # return render_template('page3.html')

def get_score(answers):
    score = 100
    for a in answers:
      if a == "45":
        print("this is a check")
        score += 100
      if a == "1776":
        print("this is a check")
        score += 100
      if a == "Federal Government":
        print("this is a check")
        score += 100
      return "Score: " + str(score)
if __name__=="__main__":
    app.run(debug=True)
