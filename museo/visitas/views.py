from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import Visita
from .forms import VisitaEntryForm,VisitaExitForm
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'index.html',{})

class Entrada(View):
    def get(self,request):
        form=VisitaEntryForm()
        context={'form':form}
        return render(request,'Entrada.html',context)

    def post(self,request):
        form=VisitaEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context={'form':form}
            return render(request,'Entrada.html',context)

class Salida(View):
    def get(self,request):
        form=VisitaExitForm()
        context={'form':form}
        return render(request,'Salida.html',context)

    def post(self,request):
        form=VisitaExitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context={'form':form}
            return render(request,'Salida.html',context)