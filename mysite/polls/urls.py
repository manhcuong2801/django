from django.urls import path


# Create url for views
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
