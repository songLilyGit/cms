from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app=Flask('sayhello')
app.config.from_pyfile('setting.py')
app.jinja_env.trim_blocks=True
app.jinja_env.lstrip_blocks=True

db=SQLAlchemy(app)
moment=Moment(app)
bootstrap=Bootstrap(app)

from sayhello import views,errors,commands
