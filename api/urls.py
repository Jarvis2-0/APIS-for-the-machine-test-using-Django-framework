from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectListView, ProjectViewSet
from .views import ProjectCreateView, AssignUsersToProjectView
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:client_pk>/projects/', ProjectViewSet.as_view({
        'post': 'create'
    }), name='client-projects'),
    

    path('clients/<int:client_pk>/projects/', ProjectViewSet.as_view({
        'get': 'list_client_projects',  # Handle GET requests to list projects
    }), name='client-projects'),


    path('clients/<int:pk>/', ClientViewSet.as_view({
        'delete': 'destroy'
    }), name='client-detail'),
    
    path('api/', include(router.urls)),
    
    path('projects/', ProjectCreateView.as_view(), name='create_project'),
    path('projects/<int:project_id>/assign_users/', AssignUsersToProjectView.as_view(), name='assign_users_to_project'),

    path('projects/', ProjectCreateView.as_view(), name='create_project'),
    path('projects/list/', ProjectListView.as_view(), name='list_projects'),

]
