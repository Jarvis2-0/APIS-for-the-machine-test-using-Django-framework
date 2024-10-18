from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import Client, Project
from .serializers import ClientSerializer, ClientCreateSerializer, ProjectSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClientSerializer
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ClientCreateSerializer
        return ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        client_id = self.kwargs.get('client_pk')
        client = Client.objects.get(id=client_id)
        serializer.save(client=client, created_by=self.request.user)

class ProjectCreateView(APIView):
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignUsersToProjectView(APIView):
    def post(self, request, project_id):
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        users = request.data.get('users', [])
        project.users.set(users)
        project.save()
        return Response({'message': 'Users assigned successfully'}, status=status.HTTP_200_OK)

class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def my_projects(self, request):
            user = request.user
            projects = user.assigned_projects.all()
            serializer = self.get_serializer(projects, many=True)
            return Response(serializer.data)
    
    
    
    @action(detail=True, methods=['get'], url_path='projects')
    def list_client_projects(self, request, pk=None):
        # Filter projects by client_id
        projects = Project.objects.filter(client_id=pk)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    


    @action(detail=True, methods=['post'], url_path='projects')
    def create_project_for_client(self, request, pk=None):
        client = Client.objects.get(pk=pk)
        project_data = request.data
        project_data['client'] = client.id
        serializer = ProjectSerializer(data=project_data)
                                       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
