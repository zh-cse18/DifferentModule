from django.contrib import admin

# Register your models here.
from .models import AddProduct


class AddProductAdmin(admin.ModelAdmin):
    fields = ['user','product_name', 'product_category', 'product_quantity', 'product_image', 'product_desc']
    #list_display = ['product_name', 'product_category', 'product_quantity', 'product_image', 'product_desc']
    list_display = [f.name for f in AddProduct._meta.get_fields()]


admin.site.register(AddProduct, AddProductAdmin)
