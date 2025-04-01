from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
   path('', views.index, name='index'),
   path('contact/',views.contact,name='contact'),
   path('home/',views.home,name='home'),
   path('contact/',views.contact,name='contact'),
   path('food/',views.food,name='food'),
   path('entertainment/',views.entertainment,name='entertainment'),
   path('visiting/',views.visiting,name='visiting'),
   path('booking/',views.booking,name='booking'),
   path('hotels/',views.hotels,name='hotels'), 
   
   path('index/', views.index, name='index'),
   path('home/', views.home, name='home'),
   path('signup/', views.signup_view, name='signup'),
   path('login/', views.login, name='login'),
   path('logout/', views.logout_view, name='logout'),
]