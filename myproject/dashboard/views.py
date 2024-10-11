#dashboard/view

from django.shortcuts import render


def my_view(request):
    # You can add any logic here
    context = {
        'message': 'ok!'
    }
    return render(request, 'example.html', context)
