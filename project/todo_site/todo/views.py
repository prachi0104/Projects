from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here.


def index(request):
    item_list=Todo.objects.filter(is_done=False).order_by("-date")#this will sort fields in descending order
    if request.method =="POST":#if method is post than we need to process the form data
        form = Todoform(request.POST) #the form data is typically sent in the request.POST dictionary. It contains the user-inputted data from the form fields. By passing request.POST to the form instance, you are instructing Django to populate the form with the data submitted in the POST request.
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = Todoform() #this returns rempty form

    page = {#this dictionary used to render items to html page in the form of context
        "forms": form,
        "list": item_list,
        "title": "TODO_LIST",
    }
    return render(request,'todo/index.html',page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.is_done = True  # Marking item as completed instead of deleting
    item.save()
    messages.info(request, "Item marked as completed!!")
    return redirect('todo')



def rescedule(request,id):
    context={}
    obj=Todo.objects.get(id=id)
    form=Updateform(request.POST or None,instance=obj)
    if request.method == "POST":
     if form.is_valid():
            form.save()
            return redirect('/')
    context['form']=form
    return render(request,'todo/resc.html',context)


def historey(request):
    context={}
    obj=Todo.objects.filter(is_done=True)
    context['data']=obj
    return render(request,'todo/historey.html',context)    



  
        






