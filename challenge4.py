from flask import Flask, Blueprint, redirect,request,abort,make_response,render_template
from stuff import flag
import sqlite3


challenge4=Blueprint('challenge4', __name__ )

#challenge 4
@challenge4.route('/challenge/4a')
def challenge4a():
    msg = request.args.get('message', '')
    return render_template('challenge4/challenge4a.html', msg=msg)


#flag logic
@challenge4.route('/challenge/4a/flag', methods=['POST'])
def flag4():
  val = flag('4a', '{1s_j4ck_ok4y}')
  if val == 'Correct':
       return redirect('/challenge/4a?message=Correct+Flag%21')
  elif val == 'empty':
       return redirect('/challenge/4a?message=Please+provide+a+valid+Flag')
  else:
       return redirect('/challenge/4a?message=Incorrect+Flag')
  

#employee login  
@challenge4.route('/challenge/4a/Login', methods=['GET', 'POST'])
def Login():
    val = request.form.get('id')
    msg = ''
    cookie = request.cookies.get('id')
    if not cookie:
        if request.method == 'GET':
            msg = ''
            return render_template('challenge4/Login.html', msg=msg)
        elif request.method == 'POST' and val != 'GR39573044274':
            msg = 'Access Denied, You either entered the wrong ID or left the field Empty'
            return render_template('challenge4/Login.html', msg=msg)
        else:
            return redirect('/challenge/4a/dashboard')
    else:
        return redirect('/challenge/4a/dashboard')

 #admin dashboard
@challenge4.route('/challenge/4a/dashboard')
def dashboard():
   response = make_response(render_template('challenge4/dashboard.html', id='GR39573044274'))
   cookie = request.cookies.get('id')
   if not cookie:
       response.set_cookie('id', 'ID#GR39573044274')
       return response
   else:
       return response
       
#lithub montior page     
@challenge4.route('/challenge/4a/dashboard/LitHubMonitor')
def lithub():
    return render_template('challenge4/LitHub.html')


#youspace monitor page
@challenge4.route('/challenge/4a/dashboard/YouSpaceMonitor')
def youspace():
    return render_template('challenge4/YouSpace.html')
@challenge4.route('/challenge/4a/Logout', methods=['POST'])
def logout():
    response = make_response(redirect('/challenge/4a/Login'))
    response.delete_cookie('id')
    return response

#secret mantis login
@challenge4.route('/challenge/4a/Mantis', methods=['POST', 'GET'])
def mantislog():
    if request.method == 'GET':
        msg=''
        return render_template('challenge4/mantis.html', msg=msg)
    else:
        id = request.form.get('id')
        password = request.form.get('password')

        connect = sqlite3.connect('mantis.db')
        cursor = connect.cursor()

        result = cursor.execute(f"SELECT * FROM mantis WHERE ID = '{id}' AND ROLE = 'OWNER' AND PASS = '{password}'")
        if result.fetchone():
            return "<h2>logedin</h2>"
        else:
            msg = "Acces Denied... Mantis is dead..."
            return render_template('challenge4/mantis.html', msg=msg)

@challenge4.route('/challenge/4a/DeadMantis')
def dead():
    abort(500)
