from flask import Flask, Blueprint, redirect,request,render_template
from stuff import flag

challenge1=Blueprint('challenge1', __name__ )

#flag logic and Briefings
@challenge1.route('/challenge/1a', methods=['POST', 'GET'])
def flag1():
    msg= ''
    if request.method == 'POST':
        val =  flag('Birkman40965070')
        if val == 'Correct':
            msg = 'correct'
            return render_template('challenge1/Contract1.html', msg=msg)
        elif val == 'empty':
            msg = 'emptey'
            return render_template('challenge1/Contract1.html', msg=msg)
        else:
            msg = 'wrong'
            return render_template('challenge1/Contract1.html', msg=msg)
    else:
        return render_template('challenge1/Contract1.html', msg=msg)
        
#main login page
@challenge1.route('/challenge/1a/Login', methods=['POST','GET'])
def main():
    msg = ''
    if request.method == 'POST':
        id = request.form.get('id')
        if id == 'JACKISTHECOOLEST':
            return render_template('challenge1/dashboard.html')
        else:
            msg='Wrong ID Please Try Again'
            return render_template('challenge1/Login.html', msg=msg)
    else:
        return render_template('challenge1/Login.html', msg=msg)



