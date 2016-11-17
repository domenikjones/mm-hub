from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.giphy_remote, name='giphy_remote'),
]