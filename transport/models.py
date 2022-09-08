from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#之后记得添加用户外键
class File(models.Model):
    filename = models.CharField(max_length=500)
    raw_data = models.FileField(upload_to='test/')
    created_time = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
