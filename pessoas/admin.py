from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter
# Register your models here.
from .models import Pessoa, FuncaoLideranca

class CustomFilter(SimpleListFilter):
    title = "Custom filter"
    parameter_name = "custom"

    def lookups(self, request, model_admin):
        return {
            ("palmeirinha", "Palmeirinha")
            ("varzea dos bois", "Varzea dos bois")
            ("bananeira", "Bananeira")
            ("laranjeira", "Laranjeira")
        }

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(povoado_text__contains=self.value())
        return queryset        


admin.site.register(Pessoa)
admin.site.register(FuncaoLideranca)