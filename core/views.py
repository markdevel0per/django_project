from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from item.models import Item, Category
from django.shortcuts import render, redirect
from .forms import SignUpForm


def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:6]
    categories = Category.objects.all()[:5]
    context = {
        'categories': categories,
        'items': items,
    }
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {"form": form})
