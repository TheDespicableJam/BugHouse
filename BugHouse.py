from flask import Flask, render_template, request, session, jsonify
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
                elif parts[0] == 'ssh@29405828' and parts[1] == '-p' and parts[2]=='jackbirkman':
                    return jsonify(
                        label='redirect',
                        data='/challenge/2a'
                    )
                elif parts[0] == 'ssh@37502750' and parts[1] == '-p' and parts[2]=='youspace':
                    return jsonify(
                        label='redirect',
                        data='/challenge/3a'
                    )
                elif parts[0] == 'ssh@47851606' and parts[1] == '-p' and parts[2]=='challenge4':
                    return jsonify(
                        label='redirect',
                        data='/challenge/4a'
                    )
                else:
                    return jsonify(
                    label='message',
                    data='Please use a valid command: "help" or "SSH"'
                )
            elif len(parts) == 1:
                if parts[0]=='help':
                    return jsonify(
                    label='message',
                    data='Use the "SSH" command to start playing, for first level: SSH@11111111 -p firstlevel<br>Use the "help" command to bring up this message'
                    )
                elif parts[0]=='ssh':
                    return jsonify(
                    label='message',
                    data='Use this format for the SSH command to start playing:<br>SSH@&lt;CHAT ID&gt; -p &lt;Admin Token&gt;<br>For first level: SSH@11111111 -p firstlevel'
                    )
                elif parts[0] == 'autopsy':
                    return jsonify(
                        label='redirect',
                        data='/autopsy'
                    )
                elif parts[0] == 'ghidra':
                    return jsonify()

                else:
                    return jsonify(
                    label='message',
                    data='Please use a valid command: "help" or "SSH"'
                )
            else:
                return jsonify(
                    label='message',
                    data='Please use a valid command: "help" or "SSH"'
                )
            
@app.route('/opwuetcbalehqo109dhbw154mnbah4l8641hn5j2ks6lrpcm69q65.onion')
def docs():
    return render_template("challenge5/documentation.html")

@app.route('/autopsy', methods=['GET', 'POST'])
def autopsy():
    if request.method =='GET':
        session['mounted'] = False
        session['scan'] = False
        session['recover'] = False
        session['drive'] = None
        return render_template('challenge5/autopsy.html')
    
    else:
        check  = request.form.get('command')
        drive = request.form.get('drive')
#part for drive selection
        if drive is not None:
            session['mounted'] = True
            if drive == "1":
                session['drive'] = '1'
                return jsonify(
                    label='SSD',
                    data='Internal SSD selected'
                )
            elif drive == "0":
                session['drive'] = '0'
                return jsonify(
                    label='HDD',
                    data='Seagate Baracuda 500GB HDD Selected'
                )
#command check
        elif not check:
            return jsonify(
                label='message',
                data='Run --help for valid commands'
            )
        else:
            command = check.lower()
            parts = command.split()
#command checking part
            if len(parts) == 1:
                if parts[0] == '--help':
                    return jsonify(
                        label='message',
                        data='Available Commands: \n--clear\n--mount\n--scan\n--recover'
                    )
#part for --mount
                elif parts[0] == '--mount':
                    return jsonify(
                        label='selector',
                        data="""<div id="selector">
                                <div>
                                    [1] Seagate Baracuda 500GB HDD  <span id="HDD" class="arrow" style="display: none;">&lt;</span>
                                </div>
                                <div>
                                    [2] Internal SSD  <span id="SDD" class="arrow" style="display: none;">&lt;</span>
                                </div>
                            </div>"""
                    )
                elif parts[0] == '--scan':
                    if not session.get('drive'):
                        return jsonify(
                            label='message',
                            data='No Drive Selected'
                        )
                    else:
                        return jsonify(
                            label='scan'
                        )
                        
#debug command                
                elif parts[0] == '--state':
                    return jsonify(
                                label='message',
                                data=f"""
                        mounted: {session.get('mounted')}
                        scan: {session.get('scan')}
                        recover: {session.get('recover')}
                        drive: {session.get('drive')}
                        """
                    )
#part for --clear
                elif parts[0] == '--clear':
                    return jsonify(
                        label='clear'
                    )
                else:
                    return jsonify(
                        label='message',
                        data='Run --help for valid commands'
                    )

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