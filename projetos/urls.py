from django.urls import path
from django.views.generic import TemplateView

app_name = "projetos"

urlpatterns = [
    path('', TemplateView.as_view(template_name="hermes/index.html"))
]
