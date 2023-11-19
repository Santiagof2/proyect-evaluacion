from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import MyModel

@receiver(post_save, sender=MyModel)
def actualizar_modelo(sender, instance, **kwargs):
    print('Se ha guardado un objeto de MiModelo')
    if instance.active:
        cache_key = 'key'
        cached_data = cache.get(cache_key, {})
        cached_data[instance.key] = instance.url
        cache.set(cache_key, cached_data)