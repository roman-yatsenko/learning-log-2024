from django.shortcuts import redirect, render

from .forms import EntryForm, TopicForm
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

def topic(request, topic_id):
    """Виводить одну тему і всі її нотатки"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Додає нову тему"""
    if request.method != 'POST':
        # Дані не відправлялись, створюється пуста форма
        form = TopicForm()
    else:
        # Обробка даних з форми
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    # Вивести пусту чи недійсну форму
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Додає нову нотатку до нової теми"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)
