from django.conf.urls import url
from newsletter.views import home, example

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^example/$', example),
    ]