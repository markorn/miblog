from django.conf.urls import include, url
from miblog import views

urlpatterns = [
    url(r'^$', views.post_list),
]