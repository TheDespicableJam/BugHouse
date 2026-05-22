from flask import Flask, Blueprint, redirect,request,make_response,render_template
from stuff import flag

challenge3=Blueprint('challenge3', __name__ )


#challenge 3
@challenge3.route('/challenge/3a')
def challenge3a():
    msg = request.args.get('message', '')
    return render_template('challenge3/challenge3a.html', msg =msg)


#flag logic
@challenge3.route('/challenge/3a/flag', methods=['POST'])
def flag3():
  val = flag('3a', '{s4v3d_th3_d4y}')
  if val == 'Correct':
       return redirect('/challenge/3a?message=Correct+Flag%21')
  elif val == 'empty':
       return redirect('/challenge/3a?message=Please+provide+a+valid+Flag')
  else:
       return redirect('/challenge/3a?message=Incorrect+Flag')
  
@challenge3.route('/challenge/3a/LitHub', methods=['GET', 'POST'])
def LitHub():
    header = request.headers.get('X-Jack-Key')

    if request.method == 'GET':
        show_post= True
        login = False
        if header == 'yes':
            login = True
            return render_template('challenge3/lithub.html', show_post=show_post, login=login)
        else:
            login=False
            return render_template('challenge3/lithub.html', login=login)
    else:
        show_post = False
        login= True
        return render_template('challenge3/lithub.html', show_post=show_post, login=login)
    
@challenge3.route('/challenge/3a/LitHub/Home/jackinbahamas', methods=['POST'])
def key():
    return "K-Wnpx-Xrl: lrf <br> I did'nt mess up this time ;)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jack"

@challenge3.route('/challenge/3a/LitHub/Home')
def Home():
    return render_template('challenge3/lithubHome.html')

    
