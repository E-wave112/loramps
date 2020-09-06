from django.db import models
from django.contrib.auth import get_user_model

from .helpers import generate_code

# Create your models here.

class Event(models.Model):
    SIZE = (
        (1, '0 - 500+'),
        (2, '600 - 1000+'),
        (3, '1000 - 1500+'),
    )

    name = models.CharField(max_length=200, unique=True)
    venue = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)
    event_code = models.CharField(max_length=6, editable=False, default=generate_code(6))
    estimated_size = models.IntegerField(choices=SIZE, default=1)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} event code: {self.event_code}'

class Ticket(models.Model):
    name = models.CharField(max_length=200)
    event_code = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_code = models.CharField(max_length=10, editable=False, default=generate_code(10))
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_code