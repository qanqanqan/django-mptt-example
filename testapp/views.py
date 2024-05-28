from django.shortcuts import render

from .models import Category


def show_categories(request):
    return render(request, "testapp/index.html", {'genres': Category.objects.all()})


def show_node(req):
    ...
