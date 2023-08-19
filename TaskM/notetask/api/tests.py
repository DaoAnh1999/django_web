from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Task

class TaskAPITest(APITestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            deadline="2023-08-31",
            status="Not Start Yet"
        )

    def test_get_all_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Test Task")

    def test_create_task(self):
        url = reverse('task-create')
        data = {
            'title': 'New Task',
            'description': 'This is a new task',
            'deadline': '2023-09-15',
            'status': 'Doing'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_update_task(self):
        url = reverse('task-update', args=[self.task.pk])
        data = {
            'title': 'Updated Task Title',
            'description': 'Updated description',
            'deadline': '2023-09-15',
            'status': 'Doing'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        url = reverse('task-delete', args=[self.task.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Task.DoesNotExist):
            self.task.refresh_from_db()