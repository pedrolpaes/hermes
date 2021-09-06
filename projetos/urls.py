from projetos.views import ProjetoDetail, ProjetosList
from django.urls import path
from django.views.generic import TemplateView

app_name = "projetos"

urlpatterns = [
    path('start/', TemplateView.as_view(template_name="hermes/index.html")),
    path('', ProjetosList .as_view(), name="Lista de projetos"),
    path('<int:pk>/', ProjetoDetail.as_view(), name="Detalhes de projeto"),
]
