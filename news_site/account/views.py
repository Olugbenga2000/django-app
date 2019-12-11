from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView
from django.urls import reverse_lazy
from account.forms import UserCreateForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
class PasswordChange(SuccessMessageMixin,PasswordChangeView):
    def get_success_url(self,**kwargs):
        success_url = reverse_lazy('post:for_user',kwargs={'username':self.kwargs.get('username')})
        return success_url
    success_message= 'Password changed successfully'   