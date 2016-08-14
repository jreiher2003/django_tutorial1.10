from django.conf.urls import url
from newsletter.views import home 

urlpatterns = [
    url(r'^$', home),
    ]