from datetime import datetime
from http.client import HTTPException
from uuid import uuid4

from flask import Flask
from flask_bootstrap import Bootstrap

from espresso.routes.api import bp as api_bp
from espresso.routes.ui import bp as ui_bp
from espresso.model import db, User, Report, Task

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@localhost:5432/postgres'

app.register_blueprint(api_bp, url_prefix='/api3')
app.register_blueprint(ui_bp, url_prefix='/')

db.init_app(app)


@app.cli.command()
def init_db():
    from espresso.model import db
    db.create_all()


@app.cli.command()
def drop_db():
    from espresso.model import db
    db.drop_all()


@app.cli.command()
def add_demo_data():
    from espresso.model import db

    demo_user = User(id=uuid4(), username='florian')
    demo_report1 = Report(id=uuid4(), user_id=demo_user.id, next_working_day=datetime(2021, 11, 22))
    demo_report2 = Report(id=uuid4(), user_id=demo_user.id, next_working_day=datetime(2021, 11, 23))
    demo_task1 = Task(id=uuid4(), description='My first Task!', done=False, tags=["demo"], report_id=demo_report1.id)
    demo_task2 = Task(id=uuid4(), description='My second Task!', done=False, tags=["demo"], report_id=demo_report1.id)
    demo_task3 = Task(id=uuid4(), description='My third Task!', done=False, tags=["demo"], report_id=demo_report2.id)
    demo_task4 = Task(id=uuid4(), description='My fourth Task!', done=False, tags=["demo"], report_id=demo_report2.id)

    db.session.add(demo_user)
    db.session.add(demo_report1)
    db.session.add(demo_report2)
    db.session.add(demo_task1)
    db.session.add(demo_task2)
    db.session.add(demo_task3)
    db.session.add(demo_task4)
    db.session.commit()
