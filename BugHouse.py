from flask import Flask, render_template, request, redirect
from challenge1 import challenge1
from challenge2 import challenge2
from challenge3 import challenge3

app=Flask(__name__)
app.register_blueprint(challenge1)
app.register_blueprint(challenge2)
app.register_blueprint(challenge3)

#home route function
@app.route('/')
def home():
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(error):
    return "Error 404 Page not found, Go Back? <br>" \
    "<a href='/'>" \
    "<button type='button'>Go Back</button></a> ", 404

@app.errorhandler(405)
def method_not_allowed(error):
    return "Error 405, This method is not allowed, Go Back? <br>" \
    "<a href='/'>" \
    "<button type='button'>Go Back</button></a> ", 405



if __name__== '__main__':
    app.run(debug=True)