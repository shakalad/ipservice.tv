from django.core.management.base import BaseCommand
from iptv_landing.utils import update_client_status, update_kz_client_status


class Command(BaseCommand):
    help = 'Updates the status of clients whose payed_until date is today'

    def handle(self, *args, **options):
        update_client_status()
        update_kz_client_status()
        self.stdout.write(self.style.SUCCESS('Client status updated successfully'))
