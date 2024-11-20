from django.db import models

class Tache(models.Model):
    objects = None
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    termine = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.titre

