from flask import Blueprint, jsonify, render_template
from sqlalchemy import select

from espresso.dto import ReportDto, TaskDto, UserDto
from espresso.model import Report, db, Task, User

bp = Blueprint('api', __name__)


@bp.route('/report', methods=['GET'])
def get_reports():
    reports = Report.query.all()
    reports = [ReportDto(r).__dict__ for r in reports]
    return jsonify(reports)


@bp.route('/report', methods=['POST'])
def add_report():
    return '', 501


@bp.route('/report/<report_id>/task', methods=['GET'])
def get_report_tasks(report_id):
    tasks = Task.query.filter_by(report_id=report_id).all()
    tasks = [TaskDto(t).__dict__ for t in tasks]
    return jsonify(tasks)


@bp.route('/report/<report_id>/task', methods=['POST'])
def post_task(report_id):
    return jsonify({
        "report_id": report_id
    })


@bp.route('/report/<report_id>/task/<task_id>', methods=['PUT'])
def put_task(report_id, task_id):
    return jsonify({
        "report_id": report_id,
        "task_id": task_id
    })


@bp.route('/task/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    return jsonify({
        "task_id": task_id
    })


@bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return jsonify(UserDto(user).__dict__)
