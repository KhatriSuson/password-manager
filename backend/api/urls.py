# api/urls.py

from django.urls import path
from . import views  # Assuming you have a 'views.py' in 'api'

urlpatterns = [
    # Example path for your API views
    path('some_view/', views.some_view, name='some_view'),
]
