#dashboard/view

from django.shortcuts import render


def my_view(request):
    # You can add any logic here
    return render(request, 'dashboard.html')
