from django.shortcuts import render


def index(request):
    context = {
        'welcome': 'Hello, world',
    }

    return render(request, 'index.html', context)
