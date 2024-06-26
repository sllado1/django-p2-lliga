from django.core.management.base import BaseCommand
from lliga.models import Equip,Lliga

class Command(BaseCommand):
    help = 'Omple els equips'

    def handle(self, *args, **kwargs):
        # Codi per omplir els equips
        # Clau forana
        nom_liga = 'Primera 24/25'  

        # Primero, obtén la instancia de Lliga asociada al nombre
        try:
            lliga_instance = Lliga.objects.get(nom=nom_liga)
        except Lliga.DoesNotExist:
            # Si no existe la liga, puedes crearla aquí o manejar el error de alguna otra manera
            raise ValueError(f"No existeix la lliga amb nom '{nom_liga}'")
        Equip.objects.create(nom='Equip1', lliga=lliga_instance, ciutat='Ciutat1')
        Equip.objects.create(nom='Equip2', lliga=lliga_instance, ciutat='Ciutat2')
        self.stdout.write(self.style.SUCCESS("Seed d'equips completat"))