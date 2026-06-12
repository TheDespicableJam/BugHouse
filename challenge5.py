from flask import Flask, Blueprint, redirect,request,abort,make_response,render_template
from stuff import flag
import sqlite3


challenge5=Blueprint('challenge5', __name__ )

@challenge5.route('/challenge/5a/Mantis', methods=['POST', 'GET'])
def mantislog():
    if request.method == 'GET':
        msg=''
        return render_template('challenge5/mantisLog.html', msg=msg)
    else:
        id = request.form.get('id')
        password = request.form.get('password')

        connect = sqlite3.connect('mantis.db')
        cursor = connect.cursor()

        result = cursor.execute(f"SELECT * FROM mantis WHERE ID = '{id}' AND ROLE = 'OWNER' AND PASS = '{password}'")
        if result.fetchone():
            return render_template('challenge5/mantisdashboard.html')
        else:
            msg = "Acces Denied... Mantis is dead..."
            return render_template('challenge5/mantisLog.html', msg=msg)

@challenge5.route('/challenge/5a/DeadMantis')
def dead():
    abort(500)