from django.db import models

# Create your models here.

class Povoado(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50, blank=True, null=True, default="Miguel Calmon")
    uf = models.CharField(max_length=50, blank=True, null=True, default="BA")
    missionário = models.OneToOneField(to='pessoas.Pessoa', 
            on_delete=models.SET_NULL, related_name='missionário', blank=True, null=True)
    ativo = models.BooleanField(default=True, null=False)
    created = models.DateField(u'Data Cadastro', auto_now=False, auto_now_add=True)
    updated = models.DateField(u'Data Atualização', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Povoados'
    