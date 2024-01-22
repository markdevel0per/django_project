from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .forms import NewItemForm, EditItemForm
from .models import Item, Category


def list_of_items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'item/items.html', {'items': items,
                                               'query': query,
                  'categories': categories,
                                               'category_id': int(category_id)})


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=pk)[:3]
    context = {
        'item': item,
        'related_items': related_items,
    }
    return render(request, 'item/detail.html', context)


@login_required(login_url='/sign-in/')
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.pk)
    else:
        form = NewItemForm()
    return render(request, 'item/form.html', {'form': form,
                                              'title': 'New Item'})


@login_required(login_url='/sign-in/')
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            # If no new image is provided, keep the existing image
            if not form.cleaned_data['image']:
                form.cleaned_data['image'] = item.image

            form.save()
            return redirect('item:detail', pk=item.pk)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {'form': form, 'title': 'Edit Item'})


@login_required(login_url='/sign-in/')
def delete(request, pk):
    item = get_object_or_404(Item, id=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')
