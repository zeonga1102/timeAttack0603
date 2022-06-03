from django.shortcuts import render
from .models import Category, Drink


# Create your views here.
def homeView(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'home.html', {'categories': categories})

    elif request.method == 'POST':
        categories = Category.objects.all()
        selected = request.POST.getlist('category')

        category = Category.objects.get(name=selected[0])
        drinks = Drink.objects.filter(category=category)

        return render(request, 'home.html', {'categories': categories, 'drinks': drinks})
