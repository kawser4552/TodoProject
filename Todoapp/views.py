from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def Homepage(request):
    todo = Employee.objects.all()
    content = {'todo':todo,'form':EmployeeForm}
    return render(request,'index.html',{'data':content})
    if request.method == "POST":
        data = request.POST
        form = EmployeeForm(data)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request,'index.html')

def Delete(request,id):
    try:
        tdata = Employee.objects.get(id = id)
        tdata.delete()
        return redirect('/')
    except:
        return redirect('/')

    return redirect('/')
        
def Updatetodo(request,id):
    try:
        tdata = Employee.objects.get(id=id)
        context = {'todo':tdata}
        return render(request,'update.html',context)
    except:
        return redirect('/')
    return redirect('/')

def update(request):
    if request.method =="POST":
        tdata = request.POST
        todo1 = tdata['todoform1']
        todo2 = tdata['todoform2']
        todo3 = tdata['todoform3']
        todoi = tdata['todoid']
        obj = Employee.objects.get(id = todoi)
        obj.name = todo1
        obj.eid=todo2
        obj.emobile=todo3
        obj.save()
        return redirect('/')
    else:
        return redirect('/')
    

