from django.db import models
from tasks.mixins import TimeStampMixin
from tasks.enums import TaskPriority, TaskStatus

class Task(TimeStampMixin):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    owner_email = models.EmailField()
    creator_email = models.EmailField()
    priority = models.IntegerField(choices=TaskPriority.choices())
    status = models.IntegerField(choices=TaskStatus.choices(), default=0)
    
    class Meta:
        db_table = 'Task'
