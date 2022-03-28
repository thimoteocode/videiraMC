from django.db import models
from povoados.models import Povoado
from django.contrib.auth.models import User

# Create your models here.
class FuncaoLideranca(models.Model):
    CATEGORIA_CHOICES = (
        ('P','Pastor'),
        ('D','Missionário'),
        ('L','Líder'),
        ('T','Diácono')
    )

    categoria = models.CharField(max_length=1, choices=CATEGORIA_CHOICES)
    descricao = models.CharField(max_length=100, blank=True)
    atribuicoes = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Função Liderança'

    def __str__(self):
        return self.descricao


class Pessoa(models.Model):
    SEXO_CHOICES = (
        ('M','Masculino'),
        ('F','Feminino'),
    )

    BATISMO_CHOICES = (
        ('S','Sim'),
        ('N','Não'),
    )

    num_cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=150)
    apelido = models.CharField(max_length=9, null=True,blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField(u'Data de Nascimento', auto_now=False, auto_now_add=False)
    celular = models.CharField(max_length=20, null=True,blank=True)
    email = models.EmailField(u'E-mail', null=True,blank=True)
    cidade = models.CharField(max_length=50, null=True,blank=True, default="Miguel Calmon")
    #rua = models.CharField(max_length=200, null=True,blank=True)
    #numero = models.IntegerField(null=True,blank=True)
    complemento = models.CharField(max_length=200, null=True,blank=True)
    #bairro = models.CharField(max_length=50, null=True,blank=True)
    #lat = models.CharField(max_length=20, null=True,blank=True)
    #lng = models.CharField(max_length=20, null=True,blank=True)
    batizado = models.CharField(max_length=1, choices=BATISMO_CHOICES, default='M')
    data_batismo = models.DateField(u'Data de Batismo', auto_now=False, auto_now_add=False, null=True)
    foto_perfil = models.FileField(upload_to='foto_perfil', blank=True, null=True)
    povoado = models.ForeignKey(Povoado, on_delete=models.PROTECT, verbose_name='Povoado')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    funcao_lideranca = models.ForeignKey(FuncaoLideranca, 
            on_delete=models.PROTECT, verbose_name='Função Liderança', blank=True, null=True)
    ativo = models.BooleanField(default=True, null=False)
    created = models.DateField(u'Data Cadastro', auto_now=False, auto_now_add=True)
    updated = models.DateField(u'Data Atualização', auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        return reverse('pessoa-list')
    
    def __str__(self):
        return self.nome