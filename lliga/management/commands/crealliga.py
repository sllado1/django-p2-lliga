from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker
from datetime import datetime, timedelta
from random import randint
 
from lliga.models import *
 
faker = Faker(["es_CA","es_ES"])
 
class Command(BaseCommand):
    help = 'Crea una lliga amb equips i jugadors'
 
    def obtenir_temporada(self,ann_actual):
        valorrand = randint(0,15)
        ara = timezone.now()
        ann_actual = ara.year-valorrand
        ann_seguent = ann_actual + 1
        temporada = f"{ann_actual}/{ann_seguent}"
        return temporada
    def obtenir_data(self, ann):
        mes = randint(1,12)
        dia = randint(1,20)
        return datetime(ann, mes, dia)

    def add_arguments(self, parser):
        parser.add_argument('titol_lliga', nargs=1, type=str)
 
    def handle(self, *args, **options):
        titol_lliga = options['titol_lliga'][0]
        lliga = Lliga.objects.filter(titol=titol_lliga)
        if lliga.count()>0:
            print("Aquesta lliga ja està creada. Posa un altre nom.")
            return
 
        print("Creem la nova lliga: {}".format(titol_lliga))
        valorrand = randint(0,15)
        ara = timezone.now()
        ann_actual = ara.year-valorrand
        strtemporada= self.obtenir_temporada(ann_actual=ann_actual);
        lliga = Lliga(  titol=titol_lliga,
                        temporada=strtemporada)
                        
        lliga.save()
 
        print("Creem equips")
        prefixos = ["RCD", "Athletic", "", "Esportiu", "Unió Esportiva"]
        for i in range(20):
            ciutat = faker.city()
            prefix = prefixos[randint(0,len(prefixos)-1)]
            if prefix:
                prefix += " "
            nom =  prefix + ciutat
            equip = Equip(ciutat=ciutat,nom=nom,lliga=lliga)
            print(equip)
            equip.save()
            lliga.equips.add(equip)
 
            print("Creem jugadors de l'equip "+nom)
            posicions=["Davanter","Porter","Migcampista","Defensa"]
            for j in range(25):
                nom = faker.first_name() + faker.last_name()
                posicio = posicions[randint(0,len(posicions)-1)]
                jugador = Jugador(nom=nom,equip=equip,posicio=posicio)
                #print(jugador)
                jugador.save()
                
 
        print("Creem partits de la lliga")
        for local in lliga.equips.all():
            for visitant in lliga.equips.all():
                if local!=visitant:
                    partit = Partit(local=local,visitant=visitant)
                    partit.local = local
                    partit.visitant = visitant
                    partit.lliga = lliga
                    partit.datainici=self.obtenir_data(ann=ann_actual)
                    partit.save()