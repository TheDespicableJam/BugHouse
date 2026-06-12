from flask import request

def flag(flg):
    flag = request.form['flag']

    if flag == flg:
        return("Correct")
    elif not flag:
        return("empty")
    else:
        return("Wrong")
    

