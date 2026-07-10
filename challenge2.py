from flask import Flask, Blueprint, redirect,request,make_response,render_template
from stuff import flag


challenge2=Blueprint('challenge2', __name__ )


#challenge 2
@challenge2.route('/challenge/aXRoaW5rdGhpc2lzdGhlcm91dGVmb3JjaGFsbGVuZ2Uy', methods=['GET', 'POST'])
def challengeaXRoaW5rdGhpc2lzdGhlcm91dGVmb3JjaGFsbGVuZ2Uy():
    msg=''
    if request.method == 'POST':
      val = flag('youspace')
      if val == 'Correct':
          msg='correct'
          response = make_response(render_template('challenge2/Contract2.html', msg=msg))
          response.delete_cookie('Role')
          return response
      elif val == 'empty':
          msg='empty'
          return render_template('challenge2/Contract2.html', msg=msg)
      else:
          msg='wrong'
          return render_template('challenge2/Contract2.html', msg=msg)
    else:
        return render_template('challenge2/Contract2.html', msg=msg)


#pick username and session checker
@challenge2.route('/challenge/aXRoaW5rdGhpc2lzdGhlcm91dGVmb3JjaGFsbGVuZ2Uy/Login')
def main():
    if request.cookies.get('Role') != None:
      return redirect('/challenge/aXRoaW5rdGhpc2lzdGhlcm91dGVmb3JjaGFsbGVuZ2Uy/YouSpace')
    else:
        return render_template('challenge2/challenge2main.html')
    


#YouSpace
@challenge2.route('/challenge/aXRoaW5rdGhpc2lzdGhlcm91dGVmb3JjaGFsbGVuZ2Uy/YouSpace', methods=['GET', 'POST'])
def YouSpace():
        login = False
        username = request.form.get('username')
        response = make_response(render_template('challenge2/youspace.html', username=username, login=login))
        if request.cookies.get('Role') == None:
            response.set_cookie('Role', 'Guest#WW91ciBhcmUgY3VycmVudGx5IGEgdXNlcg')
            return response
        elif request.cookies.get('Role') == 'Admin#WW91IGFyZSBjdXJyZW50bHkgYW4gYWRtaW4':
            login = True
            return render_template('challenge2/youspace.html', login=login)
        else:
            return response            

#/roles
@challenge2.route('/challenge/aXRoaW5rdGhpc2lzdGhlcm91dGVmb3JjaGFsbGVuZ2Uy/YouSpace/roles')
def roles():
    return render_template('challenge2/roles.html')