from sessions_exercises import views
from django.urls import path


urlpatterns = [
    path('set-session/', views.set_session),
    path('show-session/', views.show_session),
    path('delete-session/', views.delete_session),
    path('login/', views.log_greet_user),
    path('add-session/', views.add_session, name='add_session'),
    path('show-all-sessions/', views.show_multi_sessions),
]