from celery import shared_task
from celery.utils.log import get_task_logger

from tasks.models import Task

logger = get_task_logger(__name__)

    
@shared_task()   
def update_task_status(task_pk, task_status):
    
    try:
        
        logger.info('Update task status for task_id {0} to status {1}'.format(task_pk, task_status)) 
        task = Task.objects.get(pk=task_pk)
        
        task.status = task_status
        task.save()
            
    except Task.DoesNotExist:
        logger.info('Task with id: {0} does not exist, cannot update status {1}'.format(task_pk, task_status))
    
    
    
    