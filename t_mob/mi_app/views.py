# views.py
from django.http import JsonResponse
from django.views import View
from django.core.cache import cache

class TuVista(View):
    def get(self, request, *args, **kwargs):
        key = self.request.GET.get('key')
        cached_data = cache.get('key', {})
        url = cached_data.get(key)
        if url is not None:
            response_data = {'key': key, 'url': url}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Key not found in cache', 'key' : key, 'url': url}, status=404)