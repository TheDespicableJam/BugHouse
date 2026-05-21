from flask import Flask, Blueprint, redirect,request,render_template
from stuff import flag

challenge1=Blueprint('challenge1', __name__ )


# challenge 1
@challenge1.route('/challenge/1a')
def challenge1a():
    msg = request.args.get('message', '')
    return render_template('challenge1/challenge1a.html', msg=msg)


#flag logic
@challenge1.route('/challenge/1a/flag', methods=['POST'])
def flag1():
   val =  flag('1a', '{h4rd_m1st4k3}')
   if val == 'Correct':
       return redirect('/challenge/1a?message=Correct+Flag%21')
   elif val == 'empty':
       return redirect('/challenge/1a?message=Please+provide+a+valid+Flag')
   else:
       return redirect('/challenge/1a?message=Incorrect+Flag')

    
#main login page
@challenge1.route('/challenge/1a/main')
def main():
   return render_template('challenge1/challenge1main.html')


#login logic
@challenge1.route('/challenge/1a/login',methods=['POST'])
def challenge1logic():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == "REMOVEBEFOREPRODUCTION":
        return render_template('challenge1/challenge1pass.html')
    else:
       return render_template('challenge1/challenge1fail.html')

