from django.utils import timezone
from .models import Client, ClientKZ


def update_client_status():
    today = timezone.now().date()
    clients = Client.objects.filter(status=True)
    for client in clients:
        if client.payed_until < today:
            client.status = False
            client.save()


def update_kz_client_status():
    today = timezone.now().date()
    clients = ClientKZ.objects.filter(status=True)
    for client in clients:
        if client.payed_until < today:
            client.status = False
            client.save()
