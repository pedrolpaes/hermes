# Generated by Django 3.2.3 on 2021-10-08 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projetos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projetos_publicados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projeto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='projetos.categoria'),
        ),
    ]
