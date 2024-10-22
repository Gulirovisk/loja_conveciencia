from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Categorias'

    def __str__(self):
        return self.nome
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    fabricante = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='static/', blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural ="Produtos"
    def __str__(self):
        return f'(self.nome)-(self.categoria)'