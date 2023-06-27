from . import auth
from flask import render_template

import datetime
@auth.route('/cargos-info')
def login():
    now = datetime.datetime.now()
    return render_template('general-info.html',time=now)