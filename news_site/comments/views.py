from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Comment
# Create your views here.

def add_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post:single',pk=post.pk,username = post.user)
    else:
        form = CommentForm
    return render(request,'posts/_post.html',context = {'form':form})

# class CommentCreateView(CreateView):
#     model = Comment
#     template_name = "posts/_post.html"
#     form_class = CommentForm


# @login_required
# def comment_approve(request,pk):
#     comment = get_object_or_404(Comment,pk=pk)
#     comment.approve()
#     return redirect('blog_app:post_detail',pk=comment.post.pk)
    
@login_required
def delete_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post:single',pk =post_pk)

# @login_required
# def publish_post(request,pk):
#     post = get_object_or_404(Post,pk=pk)
#     post.publish()
#     return redirect('blog_app:post_detail',pk=pk)