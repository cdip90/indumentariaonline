from django.shortcuts import render
from .models import Remeras
import requests
from . import forms 
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.


def index(request):
    remeras = Remeras.objects.all()
    ctx = {"remeras": remeras}
    return render(request, "shop/index.html",ctx)
    
def contacto(request):
    return render(request, "shop/contacto.html")

def nueva_remera(request):
    if request.method == "POST":
        form = forms.FormularioRemera(request.POST)
        if form.is_valid():
            Remeras.objects.create(
            marca = form.cleaned_data["marca"],
            talle = form.cleaned_data["talle"],
            color = form.cleaned_data["color"],
            lisa = form.cleaned_data["lisa"],
            genero = form.cleaned_data["genero"]
            )
        return HttpResponseRedirect(reverse("index"))
    else:
        form = forms.FormularioRemera()
        ctx = {"form" : form}
        return render (request,"shop/nueva_remera.html", ctx)