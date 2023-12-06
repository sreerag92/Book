from django.shortcuts import render,redirect
from django.views.generic import View
from operations.forms import demo
from operations.forms import Bookform
from operations.models import book
from operations.models import std1
from operations.forms import std1form

    
class Abc(View):
   def get(self,request):
      return render(request,"abc.html")
   
   def post(self,request):
      request.POST.get("text")
      n=(request.POST["text"])
      list=[]
      string=n.casefold()
      for i in string:
         for j in range(97,123):
            if ord(i)==j:
               s=j-96
               list.append(s)
      print(list)
      return render(request,"abc.html",{"res":list})


class Home(View):
    def get(self,request):
      return render(request,"home.html")
    
class prime(View):
   def get(self,request):
      return render(request,"prime.html")
   def post(self,request):
      request.POST.get("num")
      n=int(request.POST["num"])
      if n==1:
         res= "not prime"
      elif n==2:
         res= "is prime"
      elif n > 1:
         for i in range (2,n):
            if n % i ==0:
             res="not prime"
             break
            else:
               res="is prime"
      else:
             res="enter a valid num"
      return render(request,"prime.html",{"res":res})
   
class Asg(View):
   def get(self,request):
      return render(request,"armstrong.html")
   def post(self,request):
     request.POST.get("nm")
     n=int(request.POST["nm"])
     sum=0
     temp=n
     
     while temp>0:
         digit=temp%10
         sum+=digit**3
         temp//=10
     if n==sum:
         a="is armstrong num😀"
     else:
         a="not an armstrong num😒"
     return render(request,"armstrong.html",{"st":a})
   

class demoview(View):
    def get(self,request):
      a=demo()
      return render(request,"demo.html",{"form":a})
   
    def post(self,request):
      a=demo(request.POST)
      if a.is_valid():
         print("name",a.cleaned_data["name"])
         print("mail",a.cleaned_data["email"])
      
      else:
         print("it aint valid")
      return render(request,"demo.html",{"form":a})
    
class Book(View):
   def get(self,request):
      form=Bookform()
      return render(request,"book.html",{"form":form})
   def post(self,request):
      form=Bookform(request.POST)
      if form.is_valid():
         form.save()
         form=Bookform()
#form.save():-method to add the data into db without using orm(object relational maping)query(only for modelform)
#book.ojects.create(**form.cleaned_data) ===ORM query
         print("created")
         return render(request,"book.html",{"form":form})
      else:
         return render(request,"book.html",{"form":form})
      
class Booklist(View):
   def get(self,request):
      qs = book.objects.all()
      return render(request,"booklist.html",{"qs":qs})

class Book_detailView(View):
   def get(self,request,**kwargs):
      print(kwargs)
      id = kwargs.get("pk")
      qs = book.objects.get(id=id)
      return render(request,"bookd.html",{"data":qs})

class Book_delete(View):
   def get(self,request,**kwargs):
      print(kwargs)
      id = kwargs.get("pk")
      book.objects.get(id=id).delete()
      return redirect('book-ds')
 

   
from operations.forms import Studform
from operations.models import Student

class StudView(View):
   def get(self,request):
      form=Studform()
      return render(request,"stud.html",{"form":form})
   def post(self,request):
      form=Studform(request.POST)
      if form.is_valid():
         form.save()
         form=Studform()
         print("created")
         return render(request,"stud.html",{"form":form})
      else:
         return render(request,"stud.html",{"form":form})
      
class Studlist(View):
   def get(self,request):
      qs = Student.objects.all()
      return render(request,"studlist.html",{"res":qs})

class std1view(View):
   def get(self,request):
      form=std1form()
      return render(request,"std1.html",{"form":form})
   def post(self,request):
      form=std1form(request.POST)
      if form.is_valid():
         print(form.cleaned_data)
         form.save()
         form=std1form()
         
         return render(request,"std1.html",{"form":form})
      else:
         return render(request,"std1.html",{"form":form})
      

