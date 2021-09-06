from django.db.models.query import get_prefetcher
from rest_framework import generics
from .models import Projeto
from .serializers import ProjetoSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticatedOrReadOnly

class ProjetoUserWritePermission(BasePermission):
    message = "A edição de postagens de projetos é restrita apenas ao autor."
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.autor == request.user 


class ProjetosList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  #for lists 
    queryset = Projeto.projeto_objects.all()
    serializer_class = ProjetoSerializer
    

class ProjetoDetail(generics.RetrieveUpdateDestroyAPIView, ProjetoUserWritePermission):
    permission_classes = [ProjetoUserWritePermission]
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer