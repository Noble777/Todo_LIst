from django.shortcuts import render, get_object_or_404, HttpResponsePermanentRedirect
from todolist.models import Todo

def todo_list(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            title = request.POST.get('title')
            Todo.objects.create(title=title)
    list = Todo.objects.all()

    return render(request, 'todolist.html', locals())

def complete(request, pk):
    todo_item = get_object_or_404(Todo, id=pk)
    todo_item.completed = True
    todo_item.save()
    return HttpResponsePermanentRedirect('/')

def delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    return HttpResponsePermanentRedirect('/')