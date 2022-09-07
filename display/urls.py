from django.urls import path
from .views import home

app_name = 'display'
urlpatterns = [
    path('', home, name='home'),
]
