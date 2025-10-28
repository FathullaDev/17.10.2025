from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from app.models import *



def index(request):
    categories=Categories.objects.all()
    # products=Products.objects.all()
    context={
        "categories":categories,
        # "products":products
    }
    return render(request,'index.html',context)




def category(request, pk):
    # categories = Categories.objects.filter(category_id=pk)
    # categories = Categories.objects.all()
    # category = get_object_or_404(Categories, category_id=pk)
    # products=Products.objects.all()
    categories = Categories.objects.all()
    category = get_object_or_404(Categories, pk=pk)
    products = Products.objects.filter(category=category)

    context={
        "categories": categories,
        "products": products,
        "title": "NEWS TITLE"
    }

    return render(request,'index.html',context=context)