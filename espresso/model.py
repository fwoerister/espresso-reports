import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Report(db.Model):
    __tablename__ = 'ESPRESSO_REPORT'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    timestamp = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(ForeignKey('ESPRESSO_USER.id'), nullable=False)
    next_working_day = db.Column(db.Date, nullable=False)

    tasks = relationship('Task', backref=db.backref('report'))
    user = relationship('User', backref=db.backref('reports'))


class Task(db.Model):
    __tablename__ = 'ESPRESSO_TASK'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    description = db.Column(db.String, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    tags = db.Column(db.JSON)
    report_id = db.Column(ForeignKey('ESPRESSO_REPORT.id'), nullable=False)


class User(db.Model):
    __tablename__ = 'ESPRESSO_USER'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    username = db.Column(db.String, nullable=False)
