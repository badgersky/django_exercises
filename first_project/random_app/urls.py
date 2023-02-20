from django.urls import path
from random_app import views


urlpatterns = [
    path('random/', views.view_random_number),
    path('random/<max_number>/', views.view_limited_random_number),
    path('random/<min_number>/<max_number>', views.view_random_number_between)
]

