from flask import Flask, request, render_template, flash, redirect, url_for, session, abort
import random
import openai
from datetime import date
from quotes import emotions_quotes, emotions_array
import os

f = open('secret_key.txt', "r")
secret_key = f.read()

app = Flask(__name__)
app.secret_key = secret_key
# routes and functionality of the code

users_arr = {
    'lesther' : 'lesther',
    'elijah' : 'elijah'
}





@app.route('/login', methods = ['POST', 'GET'])
def login():

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('All fields are required!', 'error')

        else:

        
            
            if username in users_arr:
                if users_arr[username] == password:
                    session['username'] = username
                        
                    return redirect(url_for('index'))
                else:
                    flash('Incorrect Password', "error")
            else:
                flash('Username not found', "error")  



            # for key in users_arr.keys():
            #     if key == username:

            #         # check password
            #         for value in users_arr.values():

            #             if value == password:
            #                 session['username'] = username
                        
            #                 return redirect(url_for('index'))

            #             elif value != password:
            #                 flash('Incorrect Password', "error")
            #     elif key != username:
            #         flash('Username not found', "error")        



    return render_template('login.html')


@app.route('/', methods = ['POST', 'GET'])

def index():


  
    is_logged_in('username')

    name = None
    emotion = None
    error = None
    if request.method == 'POST':

        name = request.form.get('name')
        emotion = request.form.get('emotion')

        if not name:
            flash("Name is required", "error")  # Add category here

        if not emotion:
            flash("Emotion is required", "error")  # Add category here

        if name and emotion:
            quotes_array_length = len(emotions_quotes.get(emotion, []))
            

            if quotes_array_length > 0:
                random_int = random.randint(0, quotes_array_length - 1)
                quote_result = emotions_quotes[emotion][random_int]

                session['name'] = name
                session['quote_result'] = quote_result

                return redirect(url_for('quote'))

    return render_template('index.html', emotions_array = emotions_array)

@app.route('/quote')
def quote():

    name = session.get('name')
    quote_result = session.get('quote_result')

    return render_template('quote_display.html', name = name, quote_result = quote_result)



# @app.errorhandler(404)
# def not_found():
#     return render_template('/error.html'), 404



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


def is_logged_in(value):

    if not session.get(value):
        abort(401)
        
    


@app.route('/user')
def current_user():
    currentUser = {
        'name': session.get('name'),
        'date': date.today(),
        'faveDog': 'Bobz'
    }

    return currentUser







if __name__ == '__main__':
    app.run(debug=True)
