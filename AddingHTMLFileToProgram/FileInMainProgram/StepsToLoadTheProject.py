'''
1.In created forlder startproject program using cmd django-admin startproject program
2.in "program" project add app using command on cmd python manage.py startapp calc
3.In urls of calc add home page path i.e. path('', views.home, name='home'),
4.In urls of main program i.e. "program" add in url from django.urls import path, include and in path 
  add path('', include('calc.urls')) to link the main project and app in it i.e is calc.
5.Add home func in views of calc
6.Add template folder where your manage.py in program
7.In Template add home.html file
8.In setting of main program add in dir  'DIRS': [os.path.join(BASE_DIR,'template')],
9.In home.html add h1 tag
10.In views of calc request render to add home.html file i.e.  return render(request,'home.html')

'''