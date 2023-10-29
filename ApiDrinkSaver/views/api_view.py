from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from ApiDrinkSaver.models.apiKey import APIKey
import uuid

@staff_member_required
def generate_api_key(request):
    user = request.user
    api_key, created = APIKey.objects.get_or_create(user=user)
    if created:
        return JsonResponse({"api_key": str(api_key.key)})
    else:
        return JsonResponse({"api_key": str(api_key.key), "detail": "La clé API existe déjà."})
