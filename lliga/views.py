from django.shortcuts import get_object_or_404, render
from .models import Lliga

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the lliga index.")

def classificacio(request, pk):
    lliga = get_object_or_404(Lliga, pk=pk)
    equips = lliga.equips.all()
    classi = []
 
    # calculem punts en llista de tuples (equip,punts)
    for equip in equips:
        punts = 0
        for partit in lliga.partit_set.filter(local=equip):
            if partit.gols_local() > partit.gols_visitant():
                punts += 3
            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
        for partit in lliga.partit_set.filter(visitant=equip):
            if partit.gols_local() < partit.gols_visitant():
                punts += 3
            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
        classi.append( (punts,equip.nom) )
    # ordenem llista
    classi.sort(reverse=True)
    return render(request,"classificacio.html",
                {
                    "classificacio":classi,
                    "nomlliga": lliga.nom,
                })

def partits(request, pk):
    lliga = get_object_or_404(Lliga, pk=pk)
    equips = lliga.equips.all()
    nelements = len(equips)
    #Crea una matriu
    classificacio= [['X' for _ in range(nelements+1)] for _ in range(nelements+1)]
    # Fem una llista de la posició dels equips
    index_equips = {equip.nom: i for i, equip in enumerate(equips)}
    classificacio[0][0]=""
    for equip in equips:
        classificacio[index_equips[equip.nom]+1][0]= equip.nom
        classificacio[0][index_equips[equip.nom]+1]=equip.nom
        for partit in lliga.partit_set.filter(local=equip):
            # Partits com a local
            classificacio[index_equips[equip.nom]+1][index_equips[partit.visitant.nom]+1]= f" {partit.gols_local()} - {partit.gols_visitant()}"
        for partit in lliga.partit_set.filter(visitant=equip):
            classificacio[index_equips[partit.local.nom]+1][index_equips[partit.visitant.nom]+1]= f" {partit.gols_local()} - {partit.gols_visitant()}"

    return render(request,"partits.html",
                    {
                        "resultats":classificacio,
                        "nomlliga": lliga.nom,
                    })
