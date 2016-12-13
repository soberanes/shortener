from django.core.management.base import BaseCommand, CommandError
from shortener.models import TackkleURL

class Command(BaseCommand):
    help = 'Refreses all TackkleURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return TackkleURL.objects.refresh_shortcodes(items=options['items'])
