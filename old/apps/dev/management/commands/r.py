from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Shortcut for running the development server'

    # def add_arguments(self, parser):
    #     parser.add_argument('settings', nargs='+', type=int)

    def handle(self, *args, **options):

        # kwargs['settings'] = 'django_jam.settings.dev'
        call_command('runserver')
