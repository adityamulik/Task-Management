from django.shortcuts import render
from django.http import HttpResponse, Http404

from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Project, Task
from .serializers import ProjectSerializer

def landing_page(request):
    return render(request, 'taskmanagement/home.html')


class ProjectList(APIView, LimitOffsetPagination):
    """
    View to list all the projects defined in the 
    get request and paginated, post request returns 
    a request and response cycle for creating a new 
    Project.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()

        projects_paginated = self.paginate_queryset(projects, request, view=self)
        serializer = ProjectSerializer(projects_paginated, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetails(APIView):
    """
    View of individual Project is retrieved using 
    the get_object function and individual project
    is retrieved, a update or edit project request
    is done using put and project is deleted using
    delete method.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ListTasks(ListModelMixin, APIView):
    pass