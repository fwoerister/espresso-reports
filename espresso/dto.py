from espresso.model import Report, User, Task


class UserDto:
    def __init__(self, user: User):
        self.id = user.id
        self.username = user.username


class ReportDto:
    def __init__(self, report: Report):
        self.id = report.id
        self.user_id = report.user_id


class TaskDto:
    def __init__(self, task: Task):
        self.id = task.id
        self.report_id = task.report_id
        self.description = task.description
        self.done = task.done
