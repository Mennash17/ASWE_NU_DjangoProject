from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.db.models import Q
from django.http import JsonResponse
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def task_list(request):
    query = request.GET.get('q', '')
    sort_field = request.GET.get('field', 'due_date') 
    sort_order = request.GET.get('order', 'asc')    
    sort_prefix = '' if sort_order == 'asc' else '-'
    category_filter = request.GET.get('category', '')
    priority_filter = request.GET.get('priority', '')

    now = timezone.now().date()
    near_date = now + timedelta(days=2)

    tasks = Task.objects.filter(user=request.user)
    if query:
        tasks = tasks.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )

    tasks = tasks.order_by(f'{sort_prefix}{sort_field}')

    if category_filter:
        tasks = tasks.filter(category__iexact=category_filter)

    if priority_filter:
        tasks = tasks.filter(priority__iexact=priority_filter)

    paginator = Paginator(tasks, 2)
    page_number = request.GET.get('page')
    category_filter = request.GET.get('category', '')
    priority_filter = request.GET.get('priority', '')
    page_obj = paginator.get_page(page_number)

    task_count = tasks.count()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')

    return render(request, 'task_list.html', {
        'form': form,
        'page_obj': page_obj,
        'query': query,
        'sort_field': sort_field,
        'sort_order': sort_order,
        'task_count': task_count,
        'category_filter': category_filter,
        'priority_filter': priority_filter,
        'now': now,
        'near_date': near_date,
    })


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_delete.html', {'task': task})


@login_required
def task_detail_json(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    data = {
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'due_date': task.due_date.strftime('%Y-%m-%d') if task.due_date else '',
        'category': task.category,
        'priority': task.priority,
    }
    return JsonResponse(data)