from django.contrib import admin
from . import models

@admin.register(models.Projeto)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'status', 'slug', 'autor', 'data_criacao')
    prepopulated_fields = {'slug':('nome',),}


admin.site.register(models.Categoria)
