from django.shortcuts import render
from django.http import HttpResponse
from djangoapp import models



def index(request):
    books = []
    for book in models.Book.objects.all():
        books.append(book.book_id)
    return HttpResponse("main")


def categories(request):
    categories = []
    for category in models.Category.objects.all():
        categories.append(category.title)
    return render(request, "categories.html", context={"categories": categories})


def books(request):
    books = []
    for book in models.Book.objects.all():
        books.append(book.title)
    return render(request, "books.html", context={"books": books})


def create_cat(request):
    if request.method == "POST":
        models.Category.objects.create(title=request.POST["title"])
        categories = []
        for category in models.Category.objects.all():
            categories.append(category.title)
        return HttpResponse("\n".join(categories))
    if request.method == "GET":
        return render(request, "create_cat.html")