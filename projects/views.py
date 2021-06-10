from .models import Project, Task
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProjectSerializer, TaskSerializer

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        project = self.request.GET.get('project', None)
        if project:
            queryset = Task.objects.filter(project=project)
        else:
            queryset = Task.objects.all()
        return queryset
    
    def create(self,request):
        data = self.request.data
        task = Task()
        project = Project.objects.get(id = data['project_id'])
        task.project = project
        task.name = data['name']
        task.description = data['description']
        task.start_date = data['start_date']
        task.end_date = data['end_date']
        task.save()
        return Response({'message':'Updated successfully'},status=200)

        
    def update(self,request,pk=None):
        data = self.request.data
        task = Task.objects.filter(id=pk).first()

        if task:
            project = Project.objects.get(id = data['project_id'])
            task.project = project
            task.name = data['name']
            task.description = data['description']
            task.start_date = data['start_date']
            task.end_date = data['end_date']
            task.save()
            return Response({'message':'Updated successfully'},status=200)
        else:
            return Response({'message':'Not Found'},status=404)