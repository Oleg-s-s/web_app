from django.shortcuts import render

def index(request):
    data = {
        'title': 'Main Page',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 20,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')