from django.urls import path
from .views import UploadView, download, delete

app_name = 'transport'
urlpatterns = [
    path('', UploadView.as_view(), name='upload'),
    path('download/<int:pk>', download, name='download'),
    path('delete/<int:pk>', delete, name='delete')
]