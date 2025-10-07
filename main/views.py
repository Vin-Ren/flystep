import datetime
from math import prod
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core import serializers
from django.utils.html import strip_tags

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import ProductForm

from .models import Product

# Create your views here.
@login_required(login_url='/login')
def render_main(req: HttpRequest):
    filters = req.GET.get('filter', 'all')
    if filters == 'mine':
        products = Product.objects.filter(user=req.user)
    else:
        products = Product.objects.all()
    
    context = {
        'person': {
            'name': 'Vincent Valentino Oei',
            'npm': '2406353225',
            'class': 'PBP E',
            'last_login': req.COOKIES.get('last_login', 'Never')
        },
        'products': products
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

@login_required(login_url='/login')
def render_edit_product(req: HttpRequest, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(req.POST or None, instance=product)

    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('main:show_main')
    ctx = {
        'form': form
    }
    return render(req, "edit_product.html", context=ctx)

@login_required(login_url='/login')
def render_delete_product(req: HttpRequest, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('main:show_main')

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

@require_POST
def register_ajax(req: HttpRequest):
    form = UserCreationForm(req.POST)
    if form.is_valid():
        user = form.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Account created successfully!',
            'username': user.username
        }, status=200)
    else:
        errors = {}
        for field, error_list in form.errors.items():
            errors[field] = [str(error) for error in error_list]
        return JsonResponse({
            'status': 'error',
            'errors': errors
        }, status=400)

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

@require_POST
def login_ajax(req: HttpRequest):
    username = req.POST.get('username')
    password = req.POST.get('password')
    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(req, user)
        return JsonResponse({
            'status': 'success',
            'message': 'Login successful!',
            'username': user.username
        }, status=200)
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid username or password'
        }, status=401)

def render_logout(req: HttpRequest):
    logout(req)
    resp = HttpResponseRedirect(reverse("main:show_main"))
    resp.delete_cookie('last_login')
    return resp

def get_products_json(req: HttpRequest):
    filters = req.GET.get('filter', 'all')
    if filters == 'mine' and req.user.is_authenticated:
        products = Product.objects.filter(user=req.user)
    else:
        products = Product.objects.all()
    
    product_list = []
    for product in products:
        product_list.append({
            'id': str(product.pk),
            'name': strip_tags(product.name),
            'description': strip_tags(product.description),
            'price': float(product.price),
            'stock': product.stock,
            'thumbnail': strip_tags(product.thumbnail),
            'is_featured': product.is_featured,
            'category': strip_tags(product.category),
            'user': product.user.username if product.user else None,
            'is_owner': req.user.is_authenticated and product.user == req.user
        })
    
    return JsonResponse({'status': 'success', 'products': product_list}, status=200)

@login_required(login_url='/login')
@require_POST
def create_product_ajax(req: HttpRequest):
    form = ProductForm(req.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = req.user
        product.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Product created successfully!',
            'product': {
                'id': str(product.id),
                'name': product.name,
                'description': product.description,
            }
        }, status=201)
    else:
        errors = {}
        for field, error_list in form.errors.items():
            errors[field] = [str(error) for error in error_list]
        return JsonResponse({
            'status': 'error',
            'errors': errors
        }, status=400)

@login_required(login_url='/login')
def edit_product_ajax(req: HttpRequest, id):
    product = get_object_or_404(Product, pk=id)
    
    if product.user != req.user:
        return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)
    
    if req.method == 'POST':
        form = ProductForm(req.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Product updated successfully!'
            }, status=200)
        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
            return JsonResponse({
                'status': 'error',
                'errors': errors
            }, status=400)
    
    # Return product data for editing
    return JsonResponse({
        'status': 'success',
        'product': {
            'id': str(product.pk),
            'name': product.name,
            'description': product.description,
            'price': float(product.price),
            'stock': product.stock,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'category': product.category,
        }
    }, status=200)

@login_required(login_url='/login')
def delete_product_ajax(req: HttpRequest, id):
    if req.method == 'DELETE':
        product = get_object_or_404(Product, pk=id)
        if product.user != req.user:
            return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)
        
        product_name = product.name
        product.delete()
        return JsonResponse({
            'status': 'success',
            'message': f'Product "{product_name}" deleted successfully!'
        }, status=200)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
