from django.contrib import admin
#from django.contrib.admin.filters import SimpleListFilter
from django.contrib.auth.admin import UserAdmin
from .models import Pessoa, FuncaoLideranca

class PessoaAdmin(UserAdmin):
    list_display = ('nome','povoado')
    search_fields = ('nome', 'povoado')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()      


admin.site.register(Pessoa)
admin.site.register(FuncaoLideranca)