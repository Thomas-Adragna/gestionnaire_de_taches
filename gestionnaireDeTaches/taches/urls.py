from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_taches, name='liste_taches'),
    path('ajouter', views.ajouter_tache, name='ajouter_tache'),
    path('terminer/<int:tache_id>/', views.terminer_tache, name='terminer_tache'),
    path('supprimer/<int:tache_id>/', views.supprimer_tache, name='supprimer_tache'),
    path('detail/<int:tache_id>/', views.detail_tache, name='detail_tache'),
]