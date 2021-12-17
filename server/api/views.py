from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DealershipRestSerializer
from .models import DealershipRest

@api_view(["GET"])
def get_api_view(request):
    api_urls = {
        "DealerShips" : "/dealership",
        "Reviews" : "/reviews",
    }
    return Response(api_urls)

@api_view(["GET"])
def get_dealership_list(request):
    dealerships_list = DealershipRest.objects.all()
    serializer_obj = DealershipRestSerializer(dealerships_list, many=True)
    return Response(serializer_obj.data)


@api_view(["POST"])
def set_dealership(request):
    serializer_obj = DealershipRestSerializer(data=request.data)
    if serializer_obj.is_valid():
        print("dealerId: ", request.data["dealerId"])
        try:
            dealer_obj = DealershipRest.objects.get(dealerId=request.data["dealerId"])
            dealer_obj.delete()
        except:
            pass
        serializer_obj.save()
    else:
        print("Object to be saved is not valid...")

    return Response(serializer_obj.data)

@api_view(["DELETE"])
def del_dealership(request, pk):
    try:
        dealer_obj = DealershipRest.objects.get(dealerId=pk)
        print("Type of dealer_obj: ", type(dealer_obj))
        dealer_obj.delete()
        return Response(f"Dealership dealerId={pk} deleted successfully!")
    except:
        return Response(f"Dealership does not exist for dealerId={pk}")

    
