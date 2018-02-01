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
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    #clear variable values and create a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/answerPage',methods=['GET','POST'])
def renderAnswerPage():
    #Check answer here
    session["answer1"] = request.form["answer1"]
    session["answer2"] = request.form["answer2"]
    session["answer3"] = request.form["answer3"]
    session["answer4"] = request.form["answer4"]
    score = 0
    if session["answer1"].lower() == "cliff burton":
        score+=1
    if session["answer2"].lower() == "the ooz":
        score+=1
    if session["answer3"].lower() == "ronnie james dio":
        score+=1
    if session["answer4"].lower() == "scotland":
        score+=1
    if "highScore" not in session:
        session["highScore"] = score
    elif score > session["highScore"]:
        session["highScore"] = score
    return render_template('answerPage.html', currentScore = score, highScore = session["highScore"])
    
if __name__=="__main__":
    app.run(debug=True)
