from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.TextField(null=True, blank=True, verbose_name='内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='作成人物')
    create_date = models.DateTimeField('作成日', auto_now_add=True, null=True)
    update_date = models.DateTimeField('更新日', auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title