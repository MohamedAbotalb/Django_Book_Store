from django.shortcuts import render, reverse, redirect, get_object_or_404

# Create your views here.
from category.models import Category
from category.forms import CategoryModelForm


def category_index(request):
    categories = Category.get_all_categories()
    return render(request, 'category/index.html', {'categories': categories})


def category_create(request):
    form = CategoryModelForm()
    if request.method == "POST":
        form = CategoryModelForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            url = reverse("category_index")
            return redirect(url)

    return render(request, 'category/create.html',
                  context={'form': form})


def category_show(request, id):
    category = Category.get_category_by_id(id)
    return render(request, 'category/show.html', {'category': category})


def category_update(request, id):
    category = Category.get_category_by_id(id)
    form = CategoryModelForm(instance=category)
    if request.method == "POST":
        form = CategoryModelForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect(category.show_url)

    return render(request, 'category/update.html', context={"form": form})


def category_delete(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    url = reverse("category_index")
    return redirect(url)
