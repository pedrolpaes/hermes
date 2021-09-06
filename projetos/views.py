from django.db.models.query import get_prefetcher
from rest_framework import generics
from .models import Projeto
from .serializers import ProjetoSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticatedOrReadOnly

class PostUserWritePermission(BasePermission):
    message = "Editing posts is restricted to the author only."
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.autor == request.user 


class ProjetosList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  #for lists 
    queryset = Projeto.projeto_objects.all()
    serializer_class = ProjetoSerializer
    

class ProjetoDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer