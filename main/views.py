from django.shortcuts import render

from .models import Product

# Create your views here.
def render_main(req):
    context = {
        'user': {
            'name': 'Vincent Valentino Oei',
            'npm': '2406353225',
            'class': 'PBP E'
        },
        'products': Product.objects.all()
    }
    
    return render(req, "main.html", context=context)
