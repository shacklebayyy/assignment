from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def crudd(request):
    data=Student.objects.all()
    print(data)
    context={"data":data}
    return render(request,"crud.html",context)

def insertData(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
       # print(name,email,age,gender)
        query = Student(name =name,email=email,age=age,gender=gender)
        query.save()
    
        messages.info(request, "Data inserted successfully")
        return redirect("/crud/")
    return render(request,"crud.html")

def UpdateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']


        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data updated successfully")
        return redirect("/crud/update/")

    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request, "edit.html", context)




