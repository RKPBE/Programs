'''
1.In created forlder startproject program using cmd django-admin startproject program
2.in "program" project add app using command on cmd python manage.py startapp calc
3.In urls of calc add home page path i.e. path('', views.home, name='home'),
4.In urls of main program i.e. "program" add in url from django.urls import path, include and in path 
  add path('', include('calc.urls')) to link the main project and app in it i.e is calc.
5.Add home func in views of calc

'''