from django.shortcuts import render

# Create your views here.
def partenaires(request):
    head_title = "Nos partenaires"
    return render(request, 'partenaires.html', {'head_title': head_title})


def videos(request):
    head_title = "Vidéos de nos partenaires"
    return render(request, 'videos.html', {'head_title': head_title})