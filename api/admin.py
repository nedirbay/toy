from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name','img')
    list_display_links = ('id','name')
    
@admin.register(models.ItemFile)
class ItemFileAdmin(admin.ModelAdmin):
    list_display = ('id','item', 'file')
    list_display_links = ('id','item', 'file')
    
admin.site.site_header = 'Toý hyzmatlary ADMIN'
admin.site.site_title = 'Toý hyzmatlary admin'
admin.site.index_title = 'Toý hyzmatlary bazalary'