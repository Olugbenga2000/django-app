from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
User = get_user_model()

#from django import template
#register = template.Library()

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length = 100,unique = True)
    slug = models.SlugField(allow_unicode= True,unique = True)
    description = models.TextField( blank = True,null = True,default = "")
    #description_html = models.TextField(editable = False,blank = True,default = '')
    #members = models.ManyToManyField(User,through='GroupMember')
    
    
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        #self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('group:detail', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['name']
    
    
# class GroupMember(models.Model):
#     user = models.ForeignKey(User,on_delete =models.CASCADE,related_name='users_group')
#     group = models.ForeignKey(Group,related_name='memberships',on_delete =models.CASCADE)
    
#     def __str__(self):
#         return self.user.username
    
#     class Meta:
#         unique_together = ('group','user')