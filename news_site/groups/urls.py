from django.urls import path
from . import views
app_name = 'group'


urlpatterns = [
    path("", views.Group_list.as_view(),name ='group_list'),
    path("new/",views.CreateGroup.as_view(),name='create'),
    path("posts/in/<slug>",views.Group_detail.as_view(), name='detail'),
    # path('join/<slug>',views.Join.as_view(), name = 'join'),
    # path('leave/<slug>',views.Leave.as_view(), name = 'leave')
    path('<slug>/delete',views.DeleteGroup.as_view(),name='delete')
] 
