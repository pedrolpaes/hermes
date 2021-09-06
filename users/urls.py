from django.urls import path
from .views import BlacklistTokenUpdateView, Criar_usuario, UsuarioList

app_name = 'users'


urlpatterns = [
    path('cadastro/', Criar_usuario.as_view(), name="criar_usuario"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
    path('', UsuarioList.as_view(), name="Lista de usuarios"),
    
]
