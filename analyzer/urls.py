from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'', views.post_list, name = "post_list"),
    re_path(r'^create/$', views.post_create, name = "post_create"),
    re_path(r'(?P<slug>[-\w]+)/$', views.post_detail, name = "post_detail"),
    # update path
    # delete path
]