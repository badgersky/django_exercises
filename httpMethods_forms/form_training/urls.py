from form_training.views import greet_user, convert_temperature
from django.urls import path


urlpatterns = [
    path('greetings/', greet_user),
    path('temp-converter/', convert_temperature),
]