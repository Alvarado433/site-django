from django.contrib import admin

from .models import app

@admin.register(app)
class adminapp(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'Date_nascimento')
