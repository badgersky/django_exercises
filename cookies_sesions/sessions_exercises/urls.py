from sessions_exercises import views
from django.urls import path


urlpatterns = [
    path('set-session/', views.set_session),
    path('show-session/', views.show_session),
    path('delete-session/', views.delete_session),
]