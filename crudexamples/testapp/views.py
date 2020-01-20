from django.shortcuts import render
from  testapp.models import Employe
def get_dumy():
    emp=Employe(id=0,name='',sal=0.0)
    return emp
def EmpCBV(request):
    return render(request,'emp.html',{'dumy':get_dumy()})
def save(request):
    id=request.POST['id']
    name=request.POST['name']
    sal=request.POST['sal']
    Empl=Employe(id=id,name=name,sal=sal)
    Emps=Employe.objects.all()
    Empl.save()
    return render(request,'emp.html',{'Emps':Emps})





# Create your views here.
