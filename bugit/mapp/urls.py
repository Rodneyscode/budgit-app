
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [
    path('', views.mainpage, name='mainpageview'),
    path('loginn/', auth_views.LoginView.as_view(template_name='loginn.html'), name='login'),
    path('logoutt/', auth_views.LogoutView.as_view(template_name='logoutt.html'), name='logout'),
    path('registerr/', views.registerr, name='reg'),
    path('contact_us/', views.contactus,  name='contact_us'),
    path('about_us/', views.aboutus, name='about_us'),
    ]