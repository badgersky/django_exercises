from calculator import views
from django.urls import path

urlpatterns = [
    path('add/<number1>/<number2>/', views.add),
    path('subtract/<number1>/<number2>/', views.subtract),
    path('multiply/<number1>/<number2>/', views.multiply),
    path('divide/<number1>/<number2>/', views.divide),
]
