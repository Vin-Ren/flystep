import datetime
from math import prod
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.core import serializers

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import ProductForm

from .models import Product

# Create your views here.
@login_required(login_url='/login')
def render_main(req: HttpRequest):
    context = {
        'user': {
            'name': 'Vincent Valentino Oei',
            'npm': '2406353225',
            'class': 'PBP E',
            'last_login': req.COOKIES.get('last_login', 'Never')
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

@login_required(login_url='/login')
def render_create_product(req: HttpRequest):
    form = ProductForm(req.POST or None)
    
    if req.method=='POST' and form.is_valid():
        product = form.save(commit=False)
        product.user = req.user
        product.save()
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

def render_register(req: HttpRequest):
    form = UserCreationForm()
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Your account has been successfully created!')
            return redirect('main:render_login')
    ctx = {
        'form':form
    }
    return render(req, 'register.html', context=ctx)

def render_login(req: HttpRequest):
    if req.method == "POST":
        form = AuthenticationForm(data=req.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            resp = HttpResponseRedirect(reverse("main:show_main"))
            resp.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            return resp
    else:
        form = AuthenticationForm(req)
    ctx = {
        'form' : form
    }
    return render(req, 'login.html', context=ctx)

def render_logout(req: HttpRequest):
    logout(req)
    resp = HttpResponseRedirect(reverse("main:show_main"))
    resp.delete_cookie('last_login')
    return resp
