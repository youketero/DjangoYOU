from django.conf.urls import url

import  gis.views
urlpatterns = [
    url(r'^$', gis.views.home, name ="home")
]