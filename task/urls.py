from django.urls import path, include

from . import api

urlpatterns = [
    path("", api.TaskList.as_view(), name="task-lists"),
    path("<int:pk>/", api.TaskDetails.as_view(), name="task-details"),
]
