from form_training.views import greet_user
from django.urls import path


urlpatterns = [
    path('greetings/', greet_user)
]