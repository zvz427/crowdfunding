from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name='手机号')
    usercategory = models.CharField(max_length=10,choices=(('company','企业'),('personal','个人')),verbose_name='用户类别',default='personal')
    
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.username