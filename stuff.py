from flask import request, redirect, render_template

def flag(flg):
    flag = request.form['flag']

    if flag == flg:
        return("Correct")
    elif not flag:
        return("empty")
    else:
        return("Wrong")
    

