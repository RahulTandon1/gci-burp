# --------------- IMPORTS ---------------
from flask import Flask, render_template, url_for, flash, \
    request, redirect

# --------------- INITIALISING STUFF ---------------
# creating the app
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('viewForm'))


@app.route('/viewForm')
def viewForm():
    return render_template('index.html')


@app.route('/submitForm', methods=['GET', 'POST'])
def submitForm():
    if request.method == 'GET':
        return redirect(url_for('viewForm'))

    username = request.form['username']
    password = request.form['password']
    amount = request.form['amount']

    resMsg = f"transferred ${amount} into {username}'s account"
    return render_template('index.html', resMsg=resMsg)



@app.route('/<anything>')
def anything(anything):
    return render_template('404.html')


app.run(debug=True)
