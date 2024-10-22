from django.contrib import admin

from .models import *

class ProdutosInline(admin.TabularInline):
    model = Produto
    extra = 1
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    inlines = [ProdutosInline]

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'fabricante', 'preco', 'categoria']
    search_fields = ['nome']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutosAdmin)