# Generated by Django 3.2.3 on 2021-10-08 01:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoria do projeto',
                'verbose_name_plural': 'Categorias dos projetos',
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('descricao', models.TextField(null=True)),
                ('conteudo', models.TextField()),
                ('orcamento', models.IntegerField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_inicio', models.DateField()),
                ('data_terminio', models.DateField()),
                ('slug', models.SlugField(max_length=250, unique_for_date='publicado')),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado')], default='publicado', max_length=10)),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
                'ordering': ('-publicado',),
            },
        ),
    ]
