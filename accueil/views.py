from django.shortcuts import render

# Create your views here.
def index(request):
    head_title = "FOIRE EXPOSITION BARBEZIEUX"
    return render(request, 'index.html', {'head_title': head_title})


def cookies(request):
    head_title = "Cookies"
    return render(request, 'cookies.html', {'head_title': head_title})


def mentions_legales(request):
    head_title = "Mentions légales"
    site_name = "foire-exposition-barbezieux.fr"
    proprietaire = "Foire Exposition de Barbezieux"
    return render(request, 'mentions_legales.html', {'head_title': head_title, 'site_name': site_name, 'proprietaire': proprietaire})