from django.test import TestCase
from tasks.tasks import update_task_status
from tasks.models import Task

class AddTestCase(TestCase):
    
    def setUp(self):
        
        Task.objects.create(title = "test task",
                                description = "testing",
                                owner_email = "abc@xyz.com",
                                creator_email = "hello@support.com",
                                priority = 0,)
    

    def testUpdateTaskStatus(self):
        
        task_id = 1
        status_id = 2
        
        update_task_status.delay(task_id,status_id).get()
        
        task = Task.objects.get(pk=task_id)
        
        self.assertEquals(task.status, status_id)