from django.contrib import admin
from users.models import Usuario
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = Usuario
    search_fields = ('email', 'user_name', 'nome',)
    list_filter = ('email', 'user_name', 'nome', 'is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'id', 'user_name', 'nome',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'nome',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('bio',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'nome', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(Usuario, UserAdminConfig)

