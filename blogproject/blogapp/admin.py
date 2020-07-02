from django.contrib import admin

# Register your models here.
from . import models
class postadmin(admin.ModelAdmin):
    list_display=['title','slug','body','author','publish','created','updated','status']
    list_filter=('status','author')
    prepopulated_fields={'slug':('title',)}
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
admin.site.register(models.Post,postadmin)