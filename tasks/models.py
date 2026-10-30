from django.db import models


class Task(models.Model):
	class Priority(models.TextChoices):
		LOW = 'low', 'Низкий'
		MEDIUM = 'medium', 'Средний'
		HIGH = 'high', 'Высокий'

	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	due_date = models.DateTimeField(null=True, blank=True)
	priority = models.CharField(
		max_length=10,
		choices=Priority.choices,
		default=Priority.MEDIUM,
	)
	completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['completed', 'due_date', '-created_at']

	def __str__(self):
		return self.title
