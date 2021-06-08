from .models import User
from .serializers import (
    UserSerializer, 
    UserDetailSerializer
)
from rest_framework import status
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated, 
    AllowAny
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        queryset = User.objects.filter(pk = self.request.user.id)
        return queryset
    
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def sign_up(self, request):
        data = request.data
        data['username'] = data['email']
        user_serializer = UserSerializer(data=data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        token = Token.objects.create(user=user)
        data['token'] = token.key
        print(user, data['token'])
        return Response({'data':data})