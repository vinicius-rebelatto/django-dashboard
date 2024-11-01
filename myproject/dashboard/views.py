#dashboard/view

from django.shortcuts import render

from .models import Article


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "year_archive.html", context)


def my_view(request):
    # You can add any logic here
    return render(request, 'dashboard.html')
