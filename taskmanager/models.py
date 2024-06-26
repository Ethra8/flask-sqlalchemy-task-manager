from taskmanager import db


class Category(db.Model):
    #schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)  # noqa unique because each category_name must be unique, nullable=False bacause it is a required field
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form  of a string
        return self.category_name


class Task(db.Model):
    #schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)  # noqa Text allows textarea with no character restraint
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)  # noqa for time: DateTime or Time
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)  # ondelete="cascade" : once category_id is deleted, all tasks with same id also get deleted (cascade)

    def __repr__(self):
        # __repr__ to represent itself in the form  of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
