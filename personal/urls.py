
from django.conf.urls import url,include
#from django.contrib import admin
from personal.models import Story
from django.views.generic import ListView, DetailView
from . import  views

urlpatterns = [
    url(r'^$', ListView.as_view(
                                    queryset=Story.objects.all(),
                                    template_name="personal/home.html")),

    url(r'personal/(?P<pk>\d+)/$', views.detailView.as_view(), name="detail"),
]

