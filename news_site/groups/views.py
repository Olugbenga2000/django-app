from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Group
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages

# Create your views here.

class CreateGroup(CreateView,LoginRequiredMixin):
    model = Group
    fields = ('name','description')
    
class Group_list(ListView):
    model = Group
    
class Group_detail(DetailView):
    model = Group
    


class DeleteGroup(DeleteView):
    model = Group
   
    
# class Join(LoginRequiredMixin,RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         return reverse('group:single', kwargs={'slug':self.kwargs.get('slug')})
    
#     def get(self, request, *args, **kwargs):
#         group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
#         try:
#            GroupMember.objects.create(group=group,user=self.request.user)
#         except :
#             messages.add_message(request, messages.WARNING, 'You are already a member!')
#         else:
#             messages.success(self.request,'You are now a member')
#         return super().get(request, *args, **kwargs)
    
    
# class Leave(LoginRequiredMixin,RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         return reverse('group:single', kwargs={'slug':self.kwargs.get('slug')})
    
#     def get(self, request, *args, **kwargs):
#         try:
#            membership = GroupMember.objects.filter(group__slug = self.kwargs.get('slug'),user=self.request.user).get()
#         except:
#             messages.warning(self.request,'You are not a member')
#         else:
#             membership.delete()
#             messages.success(self.request,'You have left the group!')
#         return super().get(request, *args, **kwargs)
        