from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


# Create your views here.


def todo_view(request):
    items = TodoItem.objects.all()
    return render(request, 'Index.html', {
        'items': items
    })


def add_todo(request):
    # check if request content is empty
    new_content = request.POST['content']
    if new_content == '':
        return HttpResponseRedirect('/todo/')

    # create todo item
    new_item = TodoItem(content=new_content)

    # save item to db
    new_item.save()
    # redirect browser to '/todo/'
    return HttpResponseRedirect('/todo/')


def delete_todo(request, todo_id):
    # get item with id
    item = TodoItem.objects.get(id=todo_id)
    # delete the item
    item.delete()
    # redirect browser to '/todo/'
    return HttpResponseRedirect('/todo/')