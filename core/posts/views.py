from django.shortcuts import render
from .models import AddProduct


def posts(request):
    product_list = AddProduct.objects.all()
    return render(request, 'posts/product-listing.html', {'all_product': product_list})


# POST DETAILS VIEW ENDPOINT
def post_details(request):
    return render(request, 'posts/blog-post.html')