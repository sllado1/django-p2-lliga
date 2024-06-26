from django.core.management.base import BaseCommand
from lliga.models import Lliga

class Command(BaseCommand):
    help = 'Omple la lliga'

    def handle(self, *args, **kwargs):
        # Codi per omplir la lliga
        Lliga.objects.create(nom='Primera 24/25', temporada='24/25')
        Lliga.objects.create(nom='Segona 24/25', temporada='24/25')
        self.stdout.write(self.style.SUCCESS("Seed de lligues completat"))