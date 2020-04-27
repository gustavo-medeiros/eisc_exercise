from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from disks.models import Artist, Album, Track
from .forms import SearchForm


def accueil(request):
    """ Afficher tous les albums de notre blog """
    form = SearchForm(request.POST or None)
    if form.is_valid():
        sujet = form.cleaned_data['sujet']

    derniers_albums = Album.objects.all()  # Nous sélectionnons tous nos articles
    to_search = ''  # not looking for anything, serves only to keep the variable from being empty
    return render(request, 'disks/accueil.html', locals())


def show_album(request, id):
    form = SearchForm(request.POST or None)
    if form.is_valid():
        sujet = form.cleaned_data['sujet']
    derniers_albums = Album.objects.all()  # Nous sélectionnons tous nos articles
    album = get_object_or_404(Album, id=id)
    return render(request, 'disks/album.html', locals())


def searching(request):
    to_search = ''
    form = SearchForm(request.GET or None)
    if form.is_valid():
        to_search = form.cleaned_data['sujet']

    derniers_albums = (Album.objects.filter(Title__contains=to_search) | Album.objects.filter(
        track__Name__contains=to_search) | Album.objects.filter(track__Composer__contains=to_search)).distinct()  # Nous
    # sélectionnons les albums trouvés
    return render(request, 'disks/accueil.html', locals())
