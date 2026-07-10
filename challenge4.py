from flask import Flask, Blueprint, redirect,request,render_template, session
from stuff import flag

employees = {
    'mndnt':{'name': 'Kevin',
            'role': 'Admin Team',
            'bio':'Silicon Valley, 2030 Asp.'},
    'ujuzks':{'name': 'Samuel',
              'role': 'Classified',
              'bio': 'None'},
    'ljkp':{'name':'Jack',
            'role': 'TERMINATED',
            'bio': 'ACCOUNT REMOVAL PENDING'}
            }

challenge4=Blueprint('challenge4', __name__ )

#flag logic
@challenge4.route('/challenge/b2theWlhbXByZXR0eXN1cmV0aGlzaXNjaGFsbGVuZ2U0', methods=['GET', 'POST'])
def challengeb2theWlhbXByZXR0eXN1cmV0aGlzaXNjaGFsbGVuZ2U0():
    if request.method == 'POST':
        val = request.form.get('flag')
        if val == 'bighack':
            session['ch4_completed'] = True
            return '[12:10 AM] <span class="apple">&lt;Rotten_Apple&gt;</span>word is on dev forums that Jack was fired... hmmm... i will contact you for the next assignment, <br> till then... LAY LOW SPEAK. TO NOBODY'
        elif not val:
            return '[12:10 AM] <span class="apple">&lt;Rotten_Apple&gt;</span>You think this is funny huh...'
        else:
            return '[12:10 AM] <span class="apple">&lt;Rotten_Apple&gt;</span>This aint the right token, keep on diggin nerd'
    else:
        return render_template('challenge4/Contract4.html')
    
@challenge4.route('/challenge/b2theWlhbXByZXR0eXN1cmV0aGlzaXNjaGFsbGVuZ2U0/Login', methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        msg=''
        return render_template('challenge4/Login.html', msg=msg)
    else:
        id = request.form.get('id').lower()
        if id in employees:
            if id == 'ljkp':
                msg= 'Access on this ID has been restricted'
                return render_template('challenge4/Login.html', msg=msg)
            else:
                return redirect(f'/challenge/b2theWlhbXByZXR0eXN1cmV0aGlzaXNjaGFsbGVuZ2U0/Dashboard?user={id}')
        else:
            msg='Wrong ID'
            return render_template('challenge4/Login.html', msg=msg)

@challenge4.route('/challenge/b2theWlhbXByZXR0eXN1cmV0aGlzaXNjaGFsbGVuZ2U0/Dashboard')
def dashboard():
    id = request.args.get('user')
    if id not in employees:
        return redirect('/challenge/b2theWlhbXByZXR0eXN1cmV0aGlzaXNjaGFsbGVuZ2U0/Login')
    else:
        bio = employees[id]['bio']
        return render_template('challenge4/dashboard.html', id=id, bio=bio)
    
@challenge4.route('/challenge/b2theWlhbXByZXR0eXN1cmV0aGlzaXNjaGFsbGVuZ2U0/Dashboard/YouSpaceMonitor')
def YSMONITOR():
    id = request.args.get('user')
    return render_template('challenge4/YouSpace.html', id=id)

@challenge4.route('/challenge/b2theWlhbXByZXR0eXN1cmV0aGlzaXNjaGFsbGVuZ2U0/Dashboard/LitHubMonitor')
def LHMONITOR():
    id = request.args.get('user')
    return render_template('challenge4/LitHub.html', id=id)

@challenge4.route('/challenge/b2theWlhbXByZXR0eXN1cmV0aGlzaXNjaGFsbGVuZ2U0/terminal', methods=['POST', 'GET'])
def terminal():
    command = request.form.get('command').lower()
    
    if not command:   
        return 'Enter a valid commmand'
    else:
        parts = command.split()
        if not parts:
            return 'Please run --help for Valid command syntax'
        else:
            if parts[0] == 'decode' and len(parts) == 5:
                if parts[2] in employees:
                    return 'Possible crack... '+employees[parts[2]]['name']
                else:
                    return 'No Possible Matches Found'
            elif parts[0] == 'analyze' and len(parts) >= 3:
                if any(part in employees for part in parts[2:]):
                    return 'Atleast one Match Found... Possible Shift: 2-9-8-5-6-7-4-3 \n Results saved to algo.txt'
                else:
                     return 'No Possible match'
            elif parts[0] == '--help':
                return 'Use the analyze command to find possible algorithms\n syntax: analyze --sample <sample1> ... <sample X>\n\n' \
                'Use the decode command to decode using algorithms found from the analyze command\nsyntax: decode --id <id> --source <algorithm file>'
            else:
                return 'Please run --help for Valid command syntax'