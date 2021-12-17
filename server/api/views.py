from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def get_api_view(request):
    api_urls = {
        "DealerShips" : "/dealership",
        "Reviews" : "/reviews",
    }
    return Response(api_urls)
