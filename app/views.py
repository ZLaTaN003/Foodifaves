from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Item
from .forms import AddItem
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    items = Item.objects.all()

    return render(request,"app/index.html",{
        "items" : items
    })


def detail(request,id):
    item = Item.objects.get(pk=id)
    return render(request,"app/detail.html",{
        "item" : item
    })
@login_required
def additem(request):
    if request.method == "POST":
        form = AddItem(request.POST, request.FILES)  
        if form.is_valid():
            itemw = form.save(commit=False)  
            itemw.user = request.user  
            itemw.save()
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = AddItem()  

    return render(request, "app/myaddform.html", {
        "form": form
    })



@login_required

def edititem(request,id):
    item = Item.objects.get(pk=id)
    form = AddItem(request.POST or None,instance=item)
    if request.user == item.user:
     if request.method == "POST":
           
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    
    return render(request,"app/myaddform.html",{
        "form": form,
        "item": item
    })
      
def delete(request,id):
     item = Item.objects.get(pk=id)
     if request.method == "POST":
         item.delete()
         return HttpResponseRedirect(reverse("index"))
     




    
