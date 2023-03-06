from django.shortcuts import render
from Database.serializers import DataSerial
from Database.models import Data

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Database.serializers import DataSerial
from rest_framework.parsers import JSONParser

@csrf_exempt
def data_List(request):
    if request.method == "GET":
        data = Data.objects.all()
        serial = DataSerial(data, many=True)
        return JsonResponse(serial.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serial = DataSerial(data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data, status=201)
        return JsonResponse(serial.errors, status=400)
    
@csrf_exempt
def data_List_Group(request, group):
    if request.method == "GET":
        qset = Data.objects.filter(group=group)
        serial = DataSerial(qset, many=True)
        return JsonResponse(serial.data, safe=False, status=201)
        
@csrf_exempt
def data_Latest(request):
    if request.method == "GET":
        qset = Data.objects.last()
        serial = DataSerial(qset)
        return JsonResponse(serial.data, safe = False, status=201)