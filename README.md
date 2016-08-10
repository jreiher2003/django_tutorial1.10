# Basic Django 1.10 tutorial 
### This readme is going to go over some basic commands to get a django python2.7 project going.  

#### Begin project
`django-admin.py startproject trydjango`  
check to see it in browser, this is using vagrant and a vm so the extra 0.0.0.0:port is needed  
`python manage.py runserver 0.0.0.0:port` --->> 127.0.0.1:port in browser  
`python manage.py migrate`   
`python manage.py createsuperuser`  put in  -u vagrant -p password  
show all available commands   
`python manage.py`  

#### Start new app  
`python manage.py startapp posts`  
---> /src/posts/models.py  
*create Post class with title content, update, timestamp, __unicode__ function*
---> /src/trydjango/settings.py   
add 'posts' to settings.py --> INSTALLED_APPS  

#### Update django application database  
`python manage.py migrate`  
`python manage.py makemigration`  
`python manage.py migrate` --> post model in database.  

#### Register Post model with admin  
---> /src/posts/admin.py  
```
from .models import Post
admin.site.register(Post)
```
---> check go to `python manage.py 0.0.0.0:8100/admin` and posts should be there.  

#### Customize admin  
[https://docs.djangoproject.com/en/1.10/ref/contrib/admin/](django admin doc)  
---> /src/posts/admin.py  
add PostModelAdmin class and add to register  
add list_display, list_display_links, and list_filters  

#### CRUD  
1.CREATE  -- POST  
2.READ    -- GET -- List / Search  
3.UPDATE  -- PUT/PATCH -- Edit  
4.DELETE  -- DELETE -- Delete  

#### Create a view -- function based views
---> /src/posts/views.py  
```
from django.http import HttpResponse
def post_create(request):
    return HttpResponse("<h1>Create!</h1>")
```
---> /src/trydjango/urls.py  
```
from django.conf.urls import url, include
from django.contrib import admin
from posts import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include(urls)),
]
```  
---> /src/posts/urls.py  
```
from django.conf.urls import url
from posts import views 

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^create/$', views.post_create, name="post_create"),
    url(r'^detail/$', views.post_detail, name="post_detail"),
    url(r'^update/$', views.post_update, name="post_update"),
    url(r'^delete/$', views.post_delete, name="post_delete"),
]
```

## Templates 
---> /root/src/settings.py add --  TEMPLATES
`'DIRS': [os.path.join(BASE_DIR, 'templates')],`  
---> /root/src/posts/views.py  
```
def post_list(request):
    return render(request, "index.html", {})
```

## QuerySet Basics - python shell related to django   
`python manage.py shell`  
```
>>>from posts.models import Post` 
>>>Post.objects.all()
<QuerySet [<Post: this is a title>, <Post: test title>]>
>>>Post.objects.filter(title="abc")
[]
>>>Post.objects.create(title="New Title", content="New Content")
<Post: New Title>
>>> Post.objects.all()
<QuerySet [<Post: this is a title>, <Post: test title>, <Post: New Title>]>
queryset = Post.objects.all()
for object in queryset:
    print object.id
    print object.title
    print object.content
```

