import json
from django.forms.models import model_to_dict
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    # instance = Product.objects.get(id=1)
    print(instance)
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=["id", 'title', 'price'])
        data = ProductSerializer(instance).data
    print(data)
    return Response(data)

# def api_home(request, *args, **kwargs):
#     print(request.GET)  # url query params
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body) # String of JSON data -> Python dict
#     except:
#         pass

#     print(data)
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type

#     return JsonResponse(data)
