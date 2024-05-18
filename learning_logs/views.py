from django.shortcuts import render

# Create your views here.

def index(request):
    """Домашня сторінка застосунку Learning Log"""
    return render(request, 'learning_logs/index.html')
