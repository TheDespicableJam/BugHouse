from flask import Flask, render_template, request, redirect, session, jsonify
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
        return """<p style="font-size:20px; margin: 0; ">You Have New Message(s)<p>
                            <ul style="padding:0; margin: 5px;">
                                <li>
                                    <button id="showmsg" onclick="showMsg()" style="border:none;">
                                        I Need Help
                                    </button>
                                </li>
                            </ul>
        <div id="messages" style="position: absolute; display: none; inset: 0; padding: 20px; background-color: rgb(80, 88, 97);">
            <div style="padding-top: 20px; font-size:20px;">
                Listen I know this might seem weirdly urgent but I need your help.<br>I used to be a dev at Bughouse, before they fired me. Some idiot kept targeting me and even when i told the "1% of the top 1%" at the company... they wouldnt understand...
                they destroyed everything, my family, my kids, my WHOLE LIFE... i want revenge.... Dont worry you'll be paid a handsome amount...
                If this works out trust me you will be able to take down one of the biggest security firms... and thats a trophy in itself...
                if you are ready click on the link... I'll be waiting...
                <br><br>
                <a href="/home"><button id="jacklink">http://opwuetcbalehqo109dhbw154mnbah4l8641hn5j2ks6lrpcm69q65.onion</button></a>
                <br><br><button id="markasread" onclick='document.getElementById("messages").style.display="none"; document.getElementById("showmsg").style.display="block"; document.getElementById("msgicon").src="/static/msgicon.png"; '>Back</button>
            </div>
        </div>"""
    else:
        return 'not completed'


@app.route('/home', methods=['GET', 'POST'])
def home():
    msg= ''
    if request.method == 'GET':
        return render_template("home.html")
    else:
        check = request.form.get('command')
        if not check:
            return jsonify(
                label='message',
                data='Please Enter a Command'
            )
        else:
            command = check.lower() 
            parts = command.split()

            if len(parts) == 3:
                if parts[0] == 'ssh@11111111' and parts[1] == '-p' and parts[2] == 'firstlevel':
                    return jsonify(
                        label='redirect',
                        data='/challenge/1a'
                    )
                else:
                    return jsonify(
                    label='message',
                    data='Please Enter a Valid Command'
                )
            else:
                return jsonify(
                    label='message',
                    data='Please Enter a Valid Command'
                )
            
@app.route('/docs')
def docs():
    return render_template("challenge5/documentation.html")

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

app.config['SECRET_KEY'] = 'POIUYTREWQLKJHGFDSAMNBVCXZQWERTYUIOPASDFGHJKLZXCVBNM'


if __name__== '__main__':
    app.run(debug=True)