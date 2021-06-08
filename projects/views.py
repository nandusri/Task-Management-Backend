from .models import Project
from rest_framework import viewsets
from .serializers import ProjectsSerializer

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = Project.objects.all()