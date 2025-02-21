from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','img')
    list_display_links = ('id','name')
    
@admin.register(models.ItemFile)
class ItemFileAdmin(admin.ModelAdmin):
    list_display = ('id','item', 'file')
    list_display_links = ('id','item', 'file')

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','username','phone','order_date')
    list_display_links = ('id','username','phone','order_date')
    search_fields = ('username',)
    ordering = ('order_date',)
    list_filter = ('username',)

@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','item__name','order__username')
    list_display_links = ('id','item__name','order__username')
    list_filter = ('order__username',)
    ordering = ('order__order_date','item__name')
    search_fields = ('order__username',)
    
admin.site.site_header = 'Toý hyzmatlary ADMIN'
admin.site.site_title = 'Toý hyzmatlary admin'
admin.site.index_title = 'Toý hyzmatlary bazalary'