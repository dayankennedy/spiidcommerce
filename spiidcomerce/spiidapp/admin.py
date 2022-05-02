from django.contrib import admin
from .models import Products
# Register your models here.

admin.site.site_header='SPIID SHOPIFY ADMIN DASH BOARD'
class ProductsAdmin(admin.ModelAdmin):
    list_display=('title','price','discount_price','category','description','image')
admin.site.register(Products,ProductsAdmin)

