from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def users(request):
    if request.method == 'GET':
        user = {
            'id': 1,
            'nome': 'Rafaél',
        }

    return JsonResponse(user, json_dumps_params={'ensure_ascii': False})