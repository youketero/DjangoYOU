from django.contrib import admin

# Register your models here.
from gis.models import Articles, point

admin.site.register(Articles)
admin.site.register(point)