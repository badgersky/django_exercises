from cookies_exercises import views
from django.urls import path


urlpatterns = [
    path('set-cookie/', views.set_cookie),
    path('show-cookie/', views.view_cookie),
    path('delete-cookie/', views.delete_cookie),
    path('set-multi-cookies/', views.add_to_cookie),
    path('show-all-cookies/', views.view_all_cookies),
]
