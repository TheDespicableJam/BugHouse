from flask import Flask, Blueprint, redirect,request,make_response,render_template
from stuff import flag

challenge4=Blueprint('challenge4', __name__ )

#challenge 3
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

 
@challenge4.route('/challenge/4a/dashboard')
def dashboard():
   response = make_response(render_template('challenge4/dashboard.html', id='GR39573044274'))
   cookie = request.cookies.get('id')
   if not cookie:
       response.set_cookie('id', 'ID#GR39573044274')
       return response
   else:
       return response
       
@challenge4.route('/challenge/4a/dashboard/LitHubMonitor')
def lithub():
    return render_template('challenge4/LitHub.html')

@challenge4.route('/challenge/4a/dashboard/YouSpaceMonitor')
def youspace():
    return render_template('challenge4/YouSpace.html')
@challenge4.route('/challenge/4a/Logout', methods=['POST'])
def logout():
    response = make_response(redirect('/challenge/4a/Login'))
    response.delete_cookie('id')
    return response

