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
    session.clear()
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/answerPage',methods=['GET','POST'])
def renderAnswerPage():
    #Check answer here
    session["answer"] = request.form["answer"]
    session["answer2"] = request.form["answer2"]
    session["answer3"] = request.form["answer3"]
    session["answer4"] = request.form["answer4"]
    score = 0
    if session["answer"].lower() == "cliff burton":
        score+=1
    elif session["answer2"].lower() == "dave mustaine":
        score+=1
    elif session["answer3"].lower() == "ronnie james dio":
        score+=1
    elif session["answer4"].lower() == "scotland":
        score+=1
    reply = 'Your score is %d /5'%(score)
    return render_template('answerPage.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=True)
