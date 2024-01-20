from item.models import Item, Category
from django.shortcuts import render


def index(request):
    items = Item.objects.filter(is_sold=False)[:5]
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'items': items,
    }
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')
