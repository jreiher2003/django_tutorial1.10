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
`python manage.py makemigrations`  
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

## Dynamic URL's 
great django url regex reference [https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md](here)
---> /src/posts/urls.py  
`url(r'^detail/(?P<id>\d+)$', views.post_detail, name="post_detail"),`
---> /src/posts/.views.py  
`def post_detail(request, id):`  
---> /src/posts/urls.py name="post_detail"
```
<a href='{% url "post_detail" id=obj.id %}'>{{ obj.title }}</a>
<a href='/posts/{{ obj.id }}'>{{ obj.title }}</a>
{% url "posts:post_detail" id=obj.id %}
<a href="{{ obj.get_absolute_url }}">{{ obj.title }}</a>
<a href='{% url "posts:post_detail" id=obj.id %}'>{{ obj.title }}</a>
```

## Model Form & Create View  
---> /src/posts/forms.py  

## Instance Update View or Edit
---> /src/posts/views.py 

## Form flash messages
## Template inheritance  
## Setup Static Files - CSS & Javascript & Images
---> /src/settings.py /src/urls.py  
`python manage.py collectstatic`  sends development static files to cdn static folder  

## Implement Bootstrap New things learnt
` <p>{{ obj.content | linebreaks | truncatechars:130 }}</p>`
`{{ obj.timestamp|timesince }}`
`{{ instance.content | linebreaks }}`
` {% cycle "" "</div><div class='col-sm-12'><hr></div><div class='row'>" %}`

## Pagination by QuerySet
[here](https://docs.djangoproject.com/en/1.9/topics/pagination/)  
`queryset = Post.objects.all().order_by("-timestamp")`  

## File Uploads with FileField and ImageField
1. models - ImageField or FileField 
2. change upload location by function 
3. html - <form enctype="multipart/form-data">  
4. views - request.FILES or None

## SlugField
plus code in vid.
1- First you have to change your urlpatterns in the posts/urls.py for something like this:
```
urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]
```
2- Go to your posts/views.py and replace (in the post_detail, post_update and post_delete) "id" for "slug".
for each functions there are 3 "id" that need to be modified.

## Social Share Links