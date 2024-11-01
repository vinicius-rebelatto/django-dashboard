#dashboard/view

from django.shortcuts import render

from .models import Article
from .models import Task
from .forms import TaskForm


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "year_archive.html", context)


def my_view(request):
    # You can add any logic here
    return render(request, 'dashboard.html')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()
    return render(request, 'tasks.html', {'form': form})