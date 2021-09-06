from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.conf import settings



class Categoria(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Categoria do projeto"
        verbose_name_plural = "Categorias dos projetos"

    def __str__(self):
        return self.name

class Projeto(models.Model):

    class ProjetoObjects(models.Manager):
        """to filter out and retrieve only publicado """
        def get_queryset(self):
            return super().get_queryset().filter(status='publicado')

    options = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )

    categoria =     models.ForeignKey(
                        Categoria, on_delete=models.PROTECT, default=1)  
    nome =          models.CharField(max_length=250)
    descricao =     models.TextField(null=True)
    conteudo =      models.TextField()
    orcamento =     models.IntegerField()
    data_criacao =  models.DateTimeField(auto_now_add=True)
    data_inicio =   models.DateField()
    data_terminio = models.DateField()
    slug =          models.SlugField(max_length=250, unique_for_date='publicado')
    publicado =     models.DateTimeField(default=timezone.now)

    # on CASCADE when delete  user deletes all his posts, maybe not the best option
    autor =         models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='projetos_publicados')
    status =        models.CharField(
        max_length=10, choices=options, default='publicado')
    
    objects = models.Manager()  # Default manager
    projeto_objects = ProjetoObjects()  # Custom manager

    class Meta:
        ordering = ("-publicado",)
        verbose_name='Projeto'
        verbose_name_plural='Projetos'

    
    def __str__(self):
        return self.nome


