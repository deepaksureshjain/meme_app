from django.urls import path
from .views import MemeApi

urlpatterns = [
    path("posts", MemeApi.as_view(), name="memes")
]
