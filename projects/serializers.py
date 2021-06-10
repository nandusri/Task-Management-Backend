from rest_framework import serializers
from .models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        

class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), write_only=True, source='project')

    class Meta:
        model = Task
        fields = '__all__'