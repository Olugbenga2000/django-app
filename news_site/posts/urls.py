from django.urls import path
from . import views
app_name = 'post'
urlpatterns = [
    path('',views.PostList.as_view(),name='all'),
    path('post/create/',views.CreatePost.as_view(),name='create'),
    path('post/by/<username>',views.UserPost.as_view(),name='for_user'),
    path('post/<username>/<int:pk>', views.PostDetail.as_view(),name = 'single'),
    path('post/<username>/<int:pk>/delete',views.PostDelete.as_view(),name = 'delete'),
    path('post/update/<username>/<int:pk>',views.UpdatePost.as_view(),name='update')
]