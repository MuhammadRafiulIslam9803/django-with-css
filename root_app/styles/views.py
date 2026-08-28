from django.shortcuts import render

# Create your views here.
def index(request):
    products = {
    'shirt': 'Formal Shirt',
    'pant': 'Jeans Pant',
    'tShirt': 'T-Shirt',
    'panjabi': 'Panjabi',
    'jacket': 'Denim Jacket',
    'sweater': 'Sweater',
    'hoodie': 'Hoodie',
    'shorts': 'Shorts',
    }
    return render(request, 'styles/index.html', {'products': products})