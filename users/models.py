from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, nome, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, nome, password, **other_fields)

    def create_user(self, email, user_name, nome, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          nome=nome, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):

    email =         models.EmailField(_('email address'), unique=True)
    user_name =     models.CharField(max_length=150, unique=True)
    nome =          models.CharField(verbose_name='Nome', max_length=150, blank=True)
    sobrenome =     models.CharField(verbose_name='Sobrenome', 
                                        max_length=50, null=True, blank=True)
    bio =           models.TextField(_('About'), max_length=500, blank=True)
    genero =        models.CharField(max_length=50, null=True, blank=True)  
    cpf =           models.IntegerField(null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    cep =           models.IntegerField(null=True, blank=True)
    cidade =        models.CharField(max_length=50, null=True, blank=True)
    estado =        models.CharField(max_length=50, null=True, blank=True)
    is_staff =      models.BooleanField(default=False)
    is_active =     models.BooleanField(default=True)
    date_joined =   models.DateTimeField(verbose_name="Data da criação", auto_now_add=True)
    last_login =    models.DateTimeField(verbose_name="Ultimo login", default=timezone.now)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'nome']

    def __str__(self):
        return self.user_name