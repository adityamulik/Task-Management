from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.settings import api_settings
from rest_framework.mixins import ListModelMixin

from .models import Project, Task
from .serializers import ProjectSerializer
from .forms import ProjectForm


class HomePage(APIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'taskmanagement/home.html'

    def get(self, request):
        """
        View returns all active projects.
        """
        queryset = Project.objects.all()
        form = ProjectForm()
        print(queryset)
        return Response({'projects': queryset, 'form': form})

    # def post(self, request, pk):
    #     """
    #     Form displayed to create a new Project
    #     """
    #     # project = get_object_or_404(Project, pk=pk)
    #     # serializer = ProjectSerializer(project, data=request.data)
    #     # if not serializer.is_valid():
    #     #     return Response({'serializer': serializer, 'project': project})
    #     # serializer.save()
    #     return redirect('taskmanagement:home')


# class ProjectCreate(View):

#     def get(self, request):
#         """ Display an HTML Form """
#         context = {"form": ProjectForm(), "update": False}
#         return render(request, "taskmangement/project/form.html", context)

#     def post(self, request):
#         """ Handle form submission: save Project """
#         project_form = ProjectForm(request.POST)
#         if project_form.is_valid():
#             project = project_form.save()
#             return redirect(project.get_absolute_url())

# API Views 

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



class TasksList(ListModelMixin, APIView):
    pass


class TasksDetail(APIView):
    pass