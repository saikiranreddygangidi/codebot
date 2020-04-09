from django.urls import path
from . import views
urlpatterns=[path('',views.home,name='register'),
          path('test',views.test,name='test'), 
          path('contact',views.contact,name='contact'),
          path('login',views.login,name='login'),
          path('logout',views.logout,name='logout'),
          path('register',views.register,name='register'),]
