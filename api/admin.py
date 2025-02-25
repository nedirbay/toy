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
    list_display = ('id', 'get_order_username', 'get_item_name')
    list_display_links = ('id', 'get_order_username', 'get_item_name')

    list_filter = ('order',) 
    ordering = ('order', 'item')  
    search_fields = ('order__username',)  

    def get_order_username(self, obj):
        return obj.order.username
    get_order_username.short_description = 'Sargyt ediji' 

    def get_item_name(self, obj):
        return obj.item.name
    get_item_name.short_description = 'Sargydy'

    
admin.site.site_header = 'Toý hyzmatlary ADMIN'
admin.site.site_title = 'Toý hyzmatlary admin'
admin.site.index_title = 'Toý hyzmatlary bazalary'