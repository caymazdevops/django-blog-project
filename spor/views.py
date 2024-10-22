from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from .models import Spor, Logolar, Kategori

def spor_list(request):
    sporlar = Spor.objects.all()  # Tüm Spor gönderilerini al
    logolar = Logolar.objects.all()
    kategoriler = Kategori.objects.all()
    return render(request, 'spor_list.html', {'sporlar': sporlar, 'logolar': logolar, 'kategoriler': kategoriler})

def team_list(request):
    logolar = Logolar.objects.all()  # Tüm Spor gönderilerini al
    return render(request, 'team_list.html', {'logolar': logolar})




def spor_detail(request, spor_id):
    spordetay = get_object_or_404(Spor, id=spor_id)  # Belirli bir Spor gönderisini al
    return render(request, 'spor_detail.html', {'spordetay': spordetay})
