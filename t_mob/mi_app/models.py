from django.db import models

# Create your models here.

class MiModelo(models.Model):
    key = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def get_redirect(key):
    try:
        return MiModelo.objects.get(key=key)
    except MiModelo.DoesNotExist:
        return {"error": "No se encontró la llave: {}".format(key)}