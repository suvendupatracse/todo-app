import pytest
from django.urls import reverse
from rest_framework.test import APITestCase

from common.factories import UserFactory
from task.models import Task
from task.factories import TaskFactory


@pytest.fixture(scope='class')
def task_params(request):
    user = UserFactory()
    request.cls.user = user
    request.cls.task_data = {"title": "test", "description": "test description here"}

@pytest.mark.tasks_test
@pytest.mark.usefixtures('task_params')
class TestTask(APITestCase):
    def test_to_create_task(self):
        self.client.force_login(self.user)
        url = reverse('task-lists')
        res = self.client.post(url, self.task_data, format='json')
        assert res.status_code == 201
        data = res.json()
        task = Task.objects.get(pk=data['id'])
        assert task.title == data['title']
        assert task.description == data['description']

    def test_to_create_task_with_invalid_data(self):
        self.client.force_login(self.user)
        task = TaskFactory(user=self.user)
        url = reverse('task-lists')
        _data = {**self.task_data, 'title':''}
        res = self.client.post(url, _data, format='json')
        assert res.status_code == 400

    def test_to_fetch_task_list(self):
        self.client.force_login(self.user)
        tasks = [TaskFactory(user=self.user) for _ in range(10)]
        url = reverse('task-lists')
        res = self.client.get(url, format='json')
        assert res.status_code == 200
        data = res.json()
        assert len(data) == len(tasks)
        
    def test_to_get_task_by_id(self):
        self.client.force_login(self.user)
        task = TaskFactory(user=self.user)
        url = reverse('task-details',kwargs={'pk': task.pk})
        res = self.client.get(url, format='json')
        assert res.status_code == 200
        data = res.json()
        assert task.title == data['title']
        assert task.description == data['description']

    def test_to_delete_task_by_id(self):
        self.client.force_login(self.user)
        task = TaskFactory(user=self.user)
        url = reverse('task-details',kwargs={'pk': task.pk})
        res = self.client.delete(url, format='json')
        assert res.status_code == 204

    def test_to_update_task_by_id(self):
        self.client.force_login(self.user)
        task = TaskFactory(user=self.user)
        url = reverse('task-details',kwargs={'pk': task.pk})
        res = self.client.put(url, self.task_data, format='json')
        assert res.status_code == 200
        data = res.json()
        assert data['title'] == self.task_data['title']

    def test_to_update_task_by_id_and_invalid_data(self):
        self.client.force_login(self.user)
        task = TaskFactory(user=self.user)
        url = reverse('task-details',kwargs={'pk': task.pk})
        _data = {**self.task_data, 'title':''}
        res = self.client.put(url, _data, format='json')
        assert res.status_code == 400