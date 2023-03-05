from class_view_exercises.views import GreetUser
from django.urls import path


urlpatterns = [
    path('say_hello/', GreetUser.as_view())
]