from class_view_exercises.views import GreetUser, TemperatureConversion
from django.urls import path


urlpatterns = [
    path('say-hello/', GreetUser.as_view()),
    path('convert-temp/', TemperatureConversion.as_view()),
]