from django.urls import path
from .views import UploadView

app_name = 'transport'
urlpatterns = [
    path('', UploadView.as_view(), name='upload'),
]