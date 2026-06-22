from flask import Flask, render_template, request, redirect, session
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

@app.route('/messages', methods=['GET'])
def msgchecker():
    check = session.get('ch4_completed')
    if check:
        return """<ul style="list-style-type: none; padding: 0;">
            <li><button id="showmsg" onclick=showMsg() style="border: none;">Get FREE RAM!!!</button></li>
        </ul>
        <div id="messages" style="position: absolute; display: none; inset: 0; padding: 20px; background-color: rgb(80, 88, 97);">
            <div>
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Architecto ea facilis veritatis eveniet saepe iure animi unde aperiam dolores! In magni rem consequatur, hic atque laboriosam corporis laborum dolorum ducimus.
                <button onclick='document.getElementById("messages").style.display="none"; document.getElementById("showmsg").style.display="block"'>Back</button>
            </div>
        </div>"""
    else:
        return 'not completed'


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
        elif command == 'ssh@47851606 -p elitehack':
            return redirect('/challenge/4a')
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

app.config['SECRET_KEY'] = 'POIUYTREWQLKJHGFDSAMNBVCXZ'


if __name__== '__main__':
    app.run(debug=True)