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
            msg = '[12:01 AM] <Rotten_Apple> Aight good work, expect us to cross paths again...'
            return render_template('challenge1/Contract1.html', msg=msg)
        elif val == 'empty':
            msg = '[12:01 AM] <Rotten_Apple> You think this is funny huh?...'
            return render_template('challenge1/Contract1.html', msg=msg)
        else:
            msg = '[12:01 AM] <Rotten_Apple> This token isnt the right one, keep on diggin nerd'
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



