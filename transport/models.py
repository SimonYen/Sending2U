from django.db import models

# Create your models here.


#之后记得添加用户外键
class File(models.Model):
    filename = models.CharField(max_length=500)
    raw_data = models.FileField(upload_to='test/')
    created_time = models.DateField(auto_now_add=True)
