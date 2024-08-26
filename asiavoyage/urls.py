from django.urls import path
from . import views

# Define a List of URL Patterns
urlpatterns = [
    path("", views.index),
    path("welcome/", views.welcome)
]
