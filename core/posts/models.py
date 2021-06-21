from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AddProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = (
        ('Technology', 'Technology'),
        ('Electronics', 'Electronics'),
        ('Grocery', 'Grocery'),)
    product_category = models.CharField(max_length=200, choices=category)
    product_name = models.CharField(max_length=200,)
    product_desc = models.TextField()
    product_quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='posts/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


