from django.urls import path, include

from . import api

urlpatterns = [
    path(
        "users/",
        api.UserViewSet.as_view({"get": "list", "post": "create"}),
        name="users",
    ),
]
