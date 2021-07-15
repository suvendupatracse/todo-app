from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from task.models import Task
from task.serializers import TaskSerializer


class TaskList(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializers = TaskSerializer

    def get(self, request):
        user = self.request.user
        serializer = self.serializers(user.task_set.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializers(data={**request.data, "user": self.request.user.pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetails(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    serializers = TaskSerializer

    def get_object(self, pk):
        user = self.request.user
        return get_object_or_404(user.task_set, id=pk)


    def get(self, request, pk):
        serializer = self.serializers(self.get_object(pk))
        return Response(serializer.data)
    
    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = self.serializers(task, data={**request.data, "user":self.request.user.pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)