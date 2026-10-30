from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class TaskApiTests(APITestCase):
	def test_create_task(self):
		response = self.client.post(
			reverse('task-list'),
			{'title': 'Подготовить презентацию', 'priority': 'high'},
			format='json',
		)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Task.objects.get().title, 'Подготовить презентацию')

	def test_list_filters_by_status_and_search(self):
		Task.objects.create(title='Купить продукты', completed=False)
		Task.objects.create(title='Записаться к врачу', completed=True)

		response = self.client.get(
			reverse('task-list'),
			{'status': 'active', 'search': 'продукты'},
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)
		self.assertEqual(response.data[0]['title'], 'Купить продукты')

	def test_update_and_delete_task(self):
		task = Task.objects.create(title='Черновик')

		update_response = self.client.patch(
			reverse('task-detail', args=[task.id]),
			{'completed': True},
			format='json',
		)
		delete_response = self.client.delete(
			reverse('task-detail', args=[task.id]),
		)

		self.assertEqual(update_response.status_code, status.HTTP_200_OK)
		self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(Task.objects.filter(id=task.id).exists())
