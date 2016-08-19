from django.conf.urls import url
from posts.views import post_list, post_create, post_detail, post_update, post_delete 

urlpatterns = [
    url(r'^$', post_list, name="post_list"),
    url(r'^create/$', post_create, name="post_create"),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name="post_detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name="delete"),
]