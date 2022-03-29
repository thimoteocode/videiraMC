from django.db import models
from povoados.models import Povoado
from pessoas.models import Pessoa

# Create your models here.
class Conexao(models.Model):
    TIPOCONEXAO_CHOICES = (
        ('A','Adultos'),
        ('J','Jovens'),
    )

    DIASEMANA_CHOICES = (
        ('1','Domingo'),
        ('2','Segunda-Feira'),
        ('3','Terça-Feira'),
        ('4','Quarta-Feira'),
        ('5','Quinta-Feira'),
        ('6','Sexta-Feira'),
        ('7','Sábado'),
    )

    nome = models.CharField(max_length=100)
    tipo_conexao = models.CharField(max_length=1, choices=TIPOCONEXAO_CHOICES)
    dia_semana_reuniao = models.CharField(max_length=1, choices=DIASEMANA_CHOICES)
    hora_reuniao = models.TimeField(max_length=6)
    povoado = models.ForeignKey(Povoado, on_delete=models.PROTECT, verbose_name='Povoado', blank=True, null=True)
    lider = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name='Líder', blank=True, null=True)
    complemento = models.TextField(max_length=200)
    #cidade = models.CharField(max_length=50, blank=True, null=True)
    participantes = models.ManyToManyField(Pessoa, on_delete=models.PROTECT, blank=True, null=True)
    ativo = models.BooleanField(default=True, null=False)
    created = models.DateField(u'Data Cadastro', auto_now=False, auto_now_add=True)
    updated = models.DateField(u'Data Atualização', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Conexão'
        verbose_name_plural = 'Conexões'

    def __str__(self):
        return self.nome