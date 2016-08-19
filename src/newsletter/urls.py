from django.conf.urls import url
from newsletter.views import home, example

urlpatterns = [
    url(r'^$', home, name="newsletter_home"),
    url(r'^example/$', example),
    ]