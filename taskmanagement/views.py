from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin

def landing_page(request):
    return render(request, 'taskmanagement/home.html')


class Home(APIView):
    pass


class ListTasks(ListModelMixin, APIView):
    pass