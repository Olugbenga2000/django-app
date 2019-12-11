from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.conf import settings
from groups.models import Group
User = get_user_model()
# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length = 100)
     text = models.TextField()
     created_at = models.DateTimeField(auto_now = True)
     user = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='posts',null = True)
     group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='posts',blank = True,null = True)
     
     #def save(self,*args,**kwargs):
         #self.text_html = misaka.html(self.text)
         #super().save(*args,**kwargs)
     def __str__(self):
          return self.title
     def get_absolute_url(self):
          return reverse('post:single', kwargs={'pk': self.pk,'username':self.user.username})
      
     class Meta:
         ordering = ['-created_at']
     
     