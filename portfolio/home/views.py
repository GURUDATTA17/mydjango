from distutils.command.upload import upload
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
  return render(request,'base.html')

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    desc = request.POST['desc']
 
    c= Contact(name=name,phone=phone,email=email,desc=desc)
    c.save()
  return render(request,'contact.html')