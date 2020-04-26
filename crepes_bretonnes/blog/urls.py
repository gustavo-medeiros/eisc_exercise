from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('', views.accueil, name='accueil'),
    #path('article/<int:id_article>', views.view_article, name='afficher_article'),
    path('article/<int:id>-<slug:slug>$', views.lire, name='lire'),
    #path('articles/<str:tag>', views.list_articles_by_tag),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('redirection', views.view_redirection),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('contact/', views.contact, name='contact'),
]