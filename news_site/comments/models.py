from django.db import models
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name = 'comments')  
    author = models.CharField(max_length = 30)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("post:single", kwargs={"pk": self.pk})
        
    def __str__(self):
        return self.text    
