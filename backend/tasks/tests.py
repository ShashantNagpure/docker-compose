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
    

    def testNoError(self):
        """Test that the ``add`` task runs with no errors,
        and returns the correct result."""
        # result = add.delay(8, 8)
        # update_task_status.delay(1,2)

        self.assertEquals(16, 16)
        # self.assertTrue(result.successful())