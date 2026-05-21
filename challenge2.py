from flask import Flask, Blueprint, redirect,request,make_response,render_template
from stuff import flag


challenge2=Blueprint('challenge2', __name__ )


#challenge 2
@challenge2.route('/challenge/2a')
def challenge2a():
    msg = request.args.get('message','')
    return render_template('challenge2/challenge2a.html', msg=msg)


#flag submission and cookie remover
@challenge2.route('/challenge/2a/flag', methods=['POST'])
def flag2():
  val = flag('2a', '{ch0c0l4t3_ch1p}')
  if val == 'Correct':
    respone = make_response(redirect('/challenge/2a?message=Correct+Flag%21'))
    respone.delete_cookie('Role')
    return respone
  elif val == 'empty':
    return redirect('/challenge/2a?message=Please+provide+a+valid+Flag')
  else:
     return redirect('/challenge/2a?message=Incorrect+Flag')
     

#pick username and session checker
@challenge2.route('/challenge/2a/main')
def main():
    if request.cookies.get('Role') != None:
      return redirect('/challenge/2a/Youspace')
    else:
        return render_template('challenge2/challenge2main.html')
    


#YouSpace
@challenge2.route('/challenge/2a/Youspace', methods=['GET', 'POST'])
def YouSpace():
        username = request.form.get('username')
        response = make_response(render_template('challenge2/youspaceUser.html', username=username))
        if request.cookies.get('Role') == None:
            response.set_cookie('Role', 'Guest#WW91ciBhcmUgY3VycmVudGx5IGEgdXNlcg')
            return response
        elif request.cookies.get('Role') == 'Admin#WW91IGFyZSBjdXJyZW50bHkgYW4gYWRtaW4':
            return render_template('challenge2/youspaceAdmin.html', )
        else:
            return response            

#/roles
@challenge2.route('/challenge/2a/roles')
def roles():
    return render_template('challenge2/roles.html')