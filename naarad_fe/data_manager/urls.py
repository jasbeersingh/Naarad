from django.urls import path
from . import views

urlpatterns = [
    # Maps the root URL '' (e.g., /data_manager/) to the landing_page view
    path('', views.landing_page, name='landing'),
]