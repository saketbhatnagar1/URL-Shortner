from django.urls import path
from .views import login_view,register,logout
urlpatterns = [
    path('',login_view,name="login_view"),
     path('register',register,name="register"),
     path('logout',logout,name='logout')
]
