from rest_framework import serializers

from task.models import Task
from common.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Task
        fields = ["id","title", "description", "user", "created_at", "updated_at"]
