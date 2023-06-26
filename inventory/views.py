from django.shortcuts import render
from .models import Manufacturer, Product, Order

# Create your views here.

# MANUFACTURER VIEW ----------------------------------------------------------
def ManufacturerView(request):
    manufacturer = Manufacturer.objects.all()
    
    return render(request, 'inventory/manufacturer.html', {"manufacturer": manufacturer})


def ManufacturerSingleView (request, post_id):

    single_manufacturer = Manufacturer.objects.get(id=post_id)
    context={
            'single_manufacturer' : single_manufacturer
        }

    return render(request,'inventory/manufacturer_single.html', context)

# PRODUCT VIEW ----------------------------------------------------------------
def ProductView(request):
    product = Product.objects.all()
    
    return render(request, 'inventory/product.html', {"product": product})


def ProductSingleView (request, post_id):

    single_product = Product.objects.get(id=post_id)
    context={
            'single_product' : single_product
        }

    return render(request,'inventory/product_single.html', context)

# ORDER VIEW ----------------------------------------------------------------
def OrderView(request):
    order = Order.objects.all()
    
    return render(request, 'inventory/order.html', {"order": order})


def OrderSingleView (request, post_id):

    single_order = Order.objects.get(id=post_id)
    context={
            'single_order' : single_order
        }

    return render(request,'inventory/order_single.html', context)