from django.shortcuts import render, redirect
from .models import Tache
from django.shortcuts import get_object_or_404

def liste_taches(request):
    taches = Tache.objects.all()
    return render(request, 'taches/liste.html', {'taches': taches})


def ajouter_tache(request):
    if request.method == 'POST':
        titre = request.POST.get('titre', '')
        description = request.POST.get('description', '')
        if titre:
            Tache.objects.create(titre=titre, description=description)
            return redirect('liste_taches')
        else:
            return render(request, 'taches/ajouter.html', {'error': 'Le titre est obligatoire.'})

    return render(request, 'taches/ajouter.html')


def terminer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    tache.termine = True
    tache.save()
    return redirect('liste_taches')


def supprimer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    tache.delete()
    return redirect('liste_taches')


def liste_taches(request):
    statut = request.GET.get('statut')  # Récupère le paramètre "statut" depuis l'URL
    if statut == 'termine':
        taches = Tache.objects.filter(termine=True)
    elif statut == 'non_termine':
        taches = Tache.objects.filter(termine=False)
    else:
        taches = Tache.objects.all()

    return render(request, 'taches/liste.html', {'taches': taches})


def detail_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    return render(request, 'taches/detail.html', {'tache': tache})
