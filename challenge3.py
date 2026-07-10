from flask import Flask, Blueprint,request,render_template
from stuff import flag

challenge3=Blueprint('challenge3', __name__ )


#challenge 3
@challenge3.route('/challenge/aXN0aGlzdGhlcm91dGVmb3JjaGFsbGVuZ2Uz', methods=['GET', 'POST'])
def challengeaXN0aGlzdGhlcm91dGVmb3JjaGFsbGVuZ2Uz():
    if request.method == 'POST':
        val = flag('privaterepos')
        if val == 'Correct':
            msg = 'correct'
            return render_template('challenge3/Contract3.html', msg=msg)
        elif val == 'empty':
            msg = 'empty'
            return render_template('challenge3/Contract3.html', msg=msg)
        else:
            msg= 'wrong'
            return render_template('challenge3/Contract3.html', msg=msg)
    else:
        msg = ''
        return render_template('challenge3/Contract3.html', msg=msg)

  
@challenge3.route('/challenge/aXN0aGlzdGhlcm91dGVmb3JjaGFsbGVuZ2Uz/LitHub')
def LitHub():
    header = request.headers.get('X-Jack-Key')
    if header == 'yes':
        return render_template('challenge3/lithub.html', user='Admin Team')
    else:
        return render_template('challenge3/lithub.html', user='LitHub Visitor')
    
@challenge3.route('/challenge/aXN0aGlzdGhlcm91dGVmb3JjaGFsbGVuZ2Uz/LitHub/backupkeys', methods=['POST'])
def key():
    return "X-Jack-Key: yes --------- I did'nt mess up this time ;) -Jack"

    
