from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
    """Домашня сторінка застосунку Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Виводить список всіх тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
