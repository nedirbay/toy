from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Banner(models.Model):
    img = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.img.url
    
    class Meta:
        db_table = 'banners'
        verbose_name = 'banner'
        verbose_name_plural = 'bannerler'
        
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Kategoriýa ady")
    img = models.ImageField(upload_to='category_images/',  verbose_name='surat saýla')
    slug = models.SlugField(blank=True,null=True, verbose_name='slug (boş durubersin)')
       
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "category"
        verbose_name = 'kategoriýa'
        verbose_name_plural = 'kategoriýalar'
        
class Item(models.Model):
    name = models.CharField(max_length=100,verbose_name='Element ady')
    img = models.ImageField(upload_to='items/', verbose_name='surat saýla')
    category = models.ForeignKey(Category,on_delete=models.PROTECT,verbose_name='Kategoriýa saýla')
    price = models.FloatField(max_length=15,default=10,verbose_name='Bahasyny giriz.(dine san giriz)')
    description = RichTextField(verbose_name='Element barada düşündiriş')
    slug = models.SlugField(blank=True,null=True, verbose_name='slug (boş durubersin)')
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)    
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "items"
        verbose_name = 'Element'
        verbose_name_plural = 'Elementler'
        
class ItemFile(models.Model):
    file = models.FileField(upload_to='item_files',verbose_name='Element faýllaryny ýükle')
    item = models.ForeignKey(Item,on_delete=models.PROTECT,related_name='files',verbose_name='Faýl elementini saýla')
    
    def __str__(self):
        return self.item.name
    
    class Meta:
        db_table = "files"
        verbose_name = 'Faýl'
        verbose_name_plural = 'Faýllar'


class Order(models.Model):
    username = models.CharField(max_length=50,blank=True,null=True,verbose_name='Sargyt ediji')
    phone = models.CharField(max_length=25, verbose_name='telefon belgisi')
    order_date = models.DateTimeField(verbose_name='gerekli senesi')

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'order'
        verbose_name = 'sargyt'
        verbose_name_plural= 'sargytlar'

class OrderItem(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE,verbose_name='Element ady')
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name='Sargyt ediji')

    def __str__(self):
        return self.order.username
    
    class Meta:
        db_table = 'orderitem'
        verbose_name = 'sargyt edilen'
        verbose_name_plural = 'sargyt edilenler'
