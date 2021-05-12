from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
import logging


# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def home(request):
    # task1 = EmployeeSign.objects.get(pk=1)
    logging.info(f"request:{dir(request)}")
    if request.method == "GET":
        result = {"name": "ghost"}
        # serializer = HomeSer(result)
        return Response(json.dumps(result))
    elif request.method == 'POST':
        result = {"name": "ghost post!"}
        return Response(json.dumps(result))
