from django.urls import path
from . import views


urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('<int:id>', views.show_album, name='show_album'),
    path('search/', views.searching, name='search'),
]