from flask import request, redirect, render_template

def flag(url ,flg):
    flag=request.form['flag']

    if flag == f'Bug{flg}':
        return("Correct")
    elif not flag:
        return("empty")
    else:
        return("Wrong")
    

