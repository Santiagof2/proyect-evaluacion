from django.http import JsonResponse
from django.views import View
from django.core.cache import cache
from .models import get_redirect  # Asegúrate de importar get_redirect aquí

class TuVista(View):
    def get(self, request, *args, **kwargs):
        key = kwargs['key']
        result = get_redirect(key)
        if isinstance(result, dict) and 'error' in result:
            return JsonResponse(result)
        else:
            data = {'key': key, 'url': result.url}
            return JsonResponse(data)