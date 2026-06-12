from flask import Flask, render_template, request, redirect
from challenge1 import challenge1
from challenge2 import challenge2
from challenge3 import challenge3
from challenge4 import challenge4
from challenge5 import challenge5

app=Flask(__name__)
app.register_blueprint(challenge1)
app.register_blueprint(challenge2)
app.register_blueprint(challenge3)
app.register_blueprint(challenge4)
app.register_blueprint(challenge5)

#home route function
@app.route('/', methods=['GET','POST'])
def desktop():
    return render_template('dekstop.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    msg= ''
    if request.method == 'GET':
        return render_template('home.html', msg=msg)
    else:
        command = str.lower(request.form.get('command'))
        if command == 'help':
           msg = 'Use the "SSH" command to start playing, for first level: SSH@11111111 -p firstlevel\nUse the "help" command to bring up this message'
           return render_template('home.html', msg=msg)
        elif command == 'ssh':
            msg = 'Use this format for the SSH command to start playing:\nSSH@<CHAT ID> -p <Admin Token>\nFor first level: SSH@11111111 -p firstlevel'
            return render_template('home.html', msg=msg)
        elif command == 'ssh@11111111 -p firstlevel':
            return redirect('/challenge/1a')
        elif command == 'ssh@29405828 -p jackbirkman':
            return redirect('/challenge/2a')
        elif command == 'ssh@37502750 -p youspace':
            return redirect('/challenge/3a')
        else:
            msg='Please use a valid command: "help" or "SSH"'
            return render_template('home.html', msg=msg)


@app.errorhandler(404)
def page_not_found(error):
    return "Error 404 Page not found, Go Back? <br>" \
    "<a href='/home'>" \
    "<button type='button'>Go Back</button></a> ", 404

@app.errorhandler(405)
def method_not_allowed(error):
    return "Error 405, This method is not allowed, Go Back? <br>" \
    "<a href='/home'>" \
    "<button type='button'>Go Back</button></a> ", 405

@app.errorhandler(500)
def server_error(error):
    return "<center>Error 500, Mantis Secure Shell Sesion Terminated, Security Breach detected, This attempt will be flagged<br>" \
    "<a href='/home'>" \
    "<button type='button'>Go Back</button></a> </center>", 500


if __name__== '__main__':
    app.run(debug=True)