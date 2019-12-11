from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from braces.views import SelectRelatedMixin
from django.http import Http404
from django.contrib import messages
from .models import Post
User = get_user_model()

# Create your views here.
class PostList(ListView,SelectRelatedMixin):
    model = Post
    select_related = ('user','group')
    
class UserPost(ListView,SelectRelatedMixin):
    model = Post
    template_name = 'posts/user_post_list.html'
    
    
    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except:
            raise Http404
        else:
            return self.post_user.posts.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context
   
class PostDetail(DetailView,SelectRelatedMixin):
    model = Post
    select_related = ('user','group')
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(CreateView,LoginRequiredMixin,SelectRelatedMixin):
    fields = ('title','text','group')
    model = Post
    
    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)  
    

class UpdatePost(UpdateView,LoginRequiredMixin,SelectRelatedMixin):
    model = Post
    fields = ('title','text','group')
  
    
class PostDelete(DeleteView,LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post:all')
        
          
    