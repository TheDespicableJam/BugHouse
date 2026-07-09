from flask import request

def flag(flg):
    check = request.form['flag']

    if not check:
        return("empty")
    else:
        flag = check.lower()    
        if flag == flg:
            return("Correct")
        else:
            return("Wrong")
    

