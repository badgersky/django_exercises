from hello_app import views
from django.urls import path


urlpatterns = [
    path('hello/', views.say_hello),
    path('hello/<name>/', views.say_personalized_hello)
]
