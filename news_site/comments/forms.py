from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
      #Metadata
   class Meta:
       model = Comment
       fields = ('author','text')
       

