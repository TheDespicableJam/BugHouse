from flask import Flask, render_template, request, redirect
from challenge1 import challenge1
from challenge2 import challenge2

app=Flask(__name__)
app.register_blueprint(challenge1)
app.register_blueprint(challenge2)


#home route function
@app.route('/')
def home():
    return render_template('home.html')



if __name__== '__main__':
    app.run(debug=True)