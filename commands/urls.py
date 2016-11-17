from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test/$', views.giphy_remote, name='giphy_remote'),
    url(r'^$', views.giphy_remote, name='giphy_remote'),
]