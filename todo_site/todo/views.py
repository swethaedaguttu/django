from django.shortcuts import render, redirect
from django.contrib import messages
from todo.forms import TodoForm
from todo.models import Todo
# Create your views here.
def home(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo')
    form = TodoForm()

    page = {
		"form": form,
		"list": item_list,
		"title": "TODO LIST",
	}
    return render(request,'index.html',page)

def remove(request, item_id):
	item = Todo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('todo')



