from django.conf.urls import url
from newsletter.views import home, contact 

urlpatterns = [
    url(r'^$', home),
    url(r'^contact/$', contact),
    ]