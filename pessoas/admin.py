from django.contrib import admin

# Register your models here.
from .models import Pessoa, FuncaoLideranca

admin.site.register(Pessoa)
admin.site.register(FuncaoLideranca)