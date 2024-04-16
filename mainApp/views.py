from django.shortcuts import render, redirect
from .models import *


def index(request):
    search = request.GET.get("search", None)
    if search is not None:
        togriSozlar = TogriSoz.objects.filter(soz=search.lower())
        if togriSozlar:
            togriSoz = togriSozlar.first()
            notogriSozlar = NotogriSoz.objects.filter(togriSoz=togriSoz)
            context = {
                "togriSoz": togriSoz,
                "notogriSozlar": notogriSozlar
            }
            return render(request, "index.html", context)
        else:
            notogriSozlar = NotogriSoz.objects.filter(soz=search.lower())
            togriSoz = notogriSozlar.first().togriSoz
            notogriSozlar = NotogriSoz.objects.filter(togriSoz=togriSoz)
            context = {
                "togriSoz": togriSoz,
                "notogriSozlar": notogriSozlar
            }
            return render(request, "index.html", context)
    return render(request, 'index.html')



