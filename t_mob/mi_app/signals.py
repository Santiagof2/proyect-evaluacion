from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import TuModelo

@receiver(post_save, sender=TuModelo)
def actualizar_modelo(sender, instance, **kwargs):
    if instance.active:
        cache.set('mi_llave', 'mi_valor')