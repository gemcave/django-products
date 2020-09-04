from django.shortcuts import render

# Create your views here.
from products.models import ProductModel


def products_page(req):
    products = {}
    if req.method == 'POST':
        if (req.POST.get('type') == 'free'):
            products = ProductModel.objects.filter(price=0)
        elif (req.POST.get('type') == 'all'):
            products = ProductModel.objects.all()
        if (req.POST.get('sold') == 'True'):
            products = ProductModel.objects.filter(sold=req.POST.get('sold'))
        if (len(req.POST.get('title')) > 0):
            products = ProductModel.objects.filter(title__contains=req.POST.get('title'))

        return render(req, 'index.html',  {'products': products})
    else:
        return render(req, 'index.html',  {'products': ProductModel.objects.all()})