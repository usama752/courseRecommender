from django.urls import path
from . import views


urlpatterns = [
	 path('register/', views.register, name="register"),
     path('login/', views.loginpage, name="login"),
     path('land/', views.home, name="home"),
    path("", views.index, name="index"),
    path('contactt/', views.contact, name='contact'),
    path('logout/', views.logoutUser, name="logout"),
    path('filter/', views.filter, name='filter'),

    
  

]