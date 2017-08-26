from django.conf.urls import url
from . import views

urlpattern = [
    #首頁（正規表達式 ^$）
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]