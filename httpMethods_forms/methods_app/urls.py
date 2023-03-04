from django.urls import path

from methods_app.views import *

urlpatterns = [
    path('generate-number/', generate_number),
]
