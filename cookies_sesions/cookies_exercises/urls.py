from cookies_sesions.cookies_exercises import views
from django.urls import path


urlpatterns = [
    path('set-cookie/', views.set_cookie)
]