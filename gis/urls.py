from django.conf.urls import url

import  gis.views
urlpatterns = [
    url(r'^$', gis.views.home, name ="home"),
    url(r'^about/$', gis.views.about, name ="about"),
    url(r'^articles/(?P<article_id>[0-9]+)/$', gis.views.show_articles, name='article')
]
