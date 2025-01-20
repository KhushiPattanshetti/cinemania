from django.shortcuts import render

def home_view(request):
    return render(request, 'first.html')

def thriller_view(request):
    return render(request, 'thriller.html')

def comedy_view(request):
    return render(request, 'comedy.html')

def action_view(request):
    return render(request, 'action.html')

def east_asian_view(request):
    return render(request, 'east_asian.html')

def family_view(request):
    return render(request, 'family.html')

def horror_view(request):
    return render(request, 'horror.html')

def romance_view(request):
    return render(request, 'romance.html')  

def teen_view(request):
    return render(request, 'teen.html')
