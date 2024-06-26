from django.core.management.base import BaseCommand
from lliga.models import Jugador

class Command(BaseCommand):
    help = 'Omple els equips'

    def handle(self, *args, **kwargs):
        # Codi per omplir els equips
        Jugador.objects.create(nom='Equip1', lliga='Primera 24/25', ciutat='Ciutat1')
        Jugador.objects.create(nom='Equip2', lliga='Primera 24/25', ciutat='Ciutat2')
        self.stdout.write(self.style.SUCCESS("Seed d'equips completat"))