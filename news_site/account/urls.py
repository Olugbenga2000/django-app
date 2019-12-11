from django.urls import path,include
from . import views
app_name = 'accounts'
urlpatterns = [
    path('Sign_up',views.SignUp.as_view(), name = 'SignUp'),
    path('<username>/passwordchange',views.PasswordChange.as_view(),name='passwordchange')
    
]