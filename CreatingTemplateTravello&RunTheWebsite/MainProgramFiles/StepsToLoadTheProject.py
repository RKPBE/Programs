'''
1.In created forlder startproject program using cmd django-admin startproject program
2.in "program" project add app using command on cmd python manage.py startapp travello
3.In urls of travello add path path('', views.index, name='index'),
4.In urls of main program change path from calc to travello path('', include('travello.urls')),
5.From the internet dowload free template of travello engency
6.Unzip the folder and add index.html file of it in template folder
7.Add a static directory in main Program and add the folders likr css img and all from unzip file of travello in this folder
8.At the last of setting of main program add 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = os.path.join(BASE_DIR,'assets')

9.Add {% static '(href,src file link)' %} in index.html file.

'''