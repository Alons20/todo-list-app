from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

# View for the index page
def index(request):
    item_list = Todo.objects.order_by("-date")  # Get all tasks ordered by date
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')  # Redirect to the main page after saving
    form = TodoForm()  # Create an empty form for new tasks

    # Prepare context data
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

# View to mark a task as done
def mark_done(request, item_id):
    item = Todo.objects.get(id=item_id)  # Get the task by its ID
    item.is_done = True  # Mark the task as done
    item.save()  # Save the change to the database
    messages.success(request, "Task marked as done!")
    return redirect('todo')  # Redirect to the todo list

# View to remove a task
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)  # Get the task by its ID
    item.delete()  # Delete the task
    messages.info(request, "Item removed!")
    return redirect('todo')  # Redirect to the todo list
