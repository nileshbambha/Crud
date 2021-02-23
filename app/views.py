from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from .models import CrudModel 
from .forms import CrudForm 
  
  
def create_view(request): 
    context ={} 
    form = CrudForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        return redirect("/")
          
    context['form']= form 
    return render(request, "create_view.html", context) 

def list_view(request): 
    context ={} 
    context["dataset"] = CrudModel.objects.all() 
          
    return render(request, "list_view.html", context) 

def detail_view(request, id): 
    context ={} 
    context["data"] = CrudModel.objects.get(id = id) 
          
    return render(request, "detail_view.html", context) 

def update_view(request, id): 
    context ={} 
    obj = get_object_or_404(CrudModel, id = id) 
    form = CrudForm(request.POST or None, instance = obj) 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id) 
    context["form"] = form 
  
    return render(request, "update_view.html", context) 

def delete_view(request, id): 
    context ={} 
    obj = get_object_or_404(CrudModel, id = id) 
    
    if request.method =="POST": 
        obj.delete() 
        return HttpResponseRedirect("/") 
  
    return render(request, "delete_view.html", context) 