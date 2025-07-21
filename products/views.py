from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def get_products(request):
    # This function would typically fetch products from the database
    list = [
        {'id': 1, 'name': 'Product 1', 'price': 10.00},
        {'id': 2, 'name': 'Product 2', 'price': 20.00},
        {'id': 3, 'name': 'Product 3', 'price': 30.00},
    ]
    return JsonResponse({'message': "Successful", 'data': list})