
from rest_framework import viewsets

from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.enums import TaskPriority,TaskStatus
from tasks.tasks import update_task_status

from tasks.post_task_create_updates import post_create_priority_to_status_transitions_map


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        
            task = serializer.save()
            task.save()
                
            # post create celery tasks for transitioning task status
            for (task_status, delay) in post_create_priority_to_status_transitions_map.get(TaskPriority(task.priority)):
                update_task_status.apply_async(args=[task.pk, TaskStatus(task_status).value],countdown=delay)


