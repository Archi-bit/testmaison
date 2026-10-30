from django.db.models import Q
from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
	serializer_class = TaskSerializer

	def get_queryset(self):
		queryset = Task.objects.all()
		status = self.request.query_params.get('status')
		search = self.request.query_params.get('search')

		if status == 'active':
			queryset = queryset.filter(completed=False)
		elif status == 'completed':
			queryset = queryset.filter(completed=True)

		if search:
			queryset = queryset.filter(
				Q(title__icontains=search) | Q(description__icontains=search)
			)

		return queryset
