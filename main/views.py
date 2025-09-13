from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core import serializers

from .forms import ProductForm

from .models import Product

# Create your views here.
def render_main(req: HttpRequest):
    context = {
        'user': {
            'name': 'Vincent Valentino Oei',
            'npm': '2406353225',
            'class': 'PBP E'
        },
        'products': Product.objects.all()
    }
    
    return render(req, "main.html", context=context)

def render_all_xml(req: HttpRequest):
    products = Product.objects.all()
    serialized = serializers.serialize('xml', products)
    return HttpResponse(serialized, content_type="application/xml")

def render_by_id_xml(req: HttpRequest, id):
    product = get_object_or_404(Product, pk=id)
    serialized = serializers.serialize('xml', [product]) # turns out it must be iterable lol, TIL.
    return HttpResponse(serialized, content_type="application/xml")

def render_all_json(req: HttpRequest):
    products = Product.objects.all()
    serialized = serializers.serialize('json', products)
    return HttpResponse(serialized, content_type="application/json")

def render_by_id_json(req: HttpRequest, id):
    product = get_object_or_404(Product, pk=id)
    serialized = serializers.serialize('json', [product]) # turns out it must be iterable lol, TIL.
    return HttpResponse(serialized, content_type="application/json")

def render_create_product(req: HttpRequest):
    form = ProductForm(req.POST or None)
    
    if req.method=='POST' and form.is_valid():
        form.save()
        return redirect('main:show_main')
    
    ctx = {
        'form': form
    }
    
    return render(req, "create_product.html", context=ctx)

def render_product_details(req: HttpRequest, id):
    product = get_object_or_404(Product, pk=id)
    ctx = {
        'product': product
    }
    return render(req, 'details.html', context=ctx)
