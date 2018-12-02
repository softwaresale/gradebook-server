from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import GradeSerializer
from .models import Grade

# Create your views here.

@csrf_exempt
def grades_list(request):
    if request.method == "GET":
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many = True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = GradeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def grades_detail(request, pk):
    try:
        grade = Grade.objects.get(pk=pk)
    except Exception as e:
        return HttpRequest(e, status=404, content_type="text/plain")

    if request.method == "GET":
        serializer = GradeSerializer(grade)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = GradeSerializer(grade, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)
