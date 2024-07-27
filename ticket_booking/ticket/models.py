from django.db import models

# Create your models here.

class TicketBook(models.Model):
    CHOICES = [('Ac', 'Ac'), ('Non-Ac', 'Non-Ac')]
    ticket_no = models.IntegerField()
    from_place = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travelling_date = models.DateTimeField()
    bus_type = models.CharField(max_length=50, choices=CHOICES)
    amount = models.FloatField()
