from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DealershipRestSerializer, ReviewRestSerializer
from .models import DealershipRest, ReviewRest
import json


@api_view(["GET"])
def get_dealership_with_state(request):
    if "state" in request.GET:
        state_i = request.GET.get("state")
        dealerships_list = DealershipRest.objects.all().filter(st=state_i)
        serializer_obj = DealershipRestSerializer(dealerships_list, many=True)
        return HttpResponse(json.dumps(serializer_obj.data, indent=2), content_type="application/json")
        print(f"Found state: {state_i}")
    else:
        print("State not given in field...")
    try:
        dealer_obj = DealershipRest.objects.get(st=state_code)
        print(f"Found objects for state={state_code}")
    except:
        pass

    return render(request, 'djangoapp/about.html')


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

@api_view(["GET"])
def get_reviews_list(request):
    reviews_list = ReviewRest.objects.all()
    serializer_obj = ReviewRestSerializer(reviews_list, many=True)
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


