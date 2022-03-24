# Generated by Django 4.0.3 on 2022-03-24 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FuncaoLideranca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('P', 'Pastor'), ('D', 'Missionário'), ('L', 'Líder'), ('T', 'Diácono')], max_length=1)),
                ('descricao', models.CharField(blank=True, max_length=100)),
                ('atribuicoes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Função Liderança',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cpf', models.CharField(max_length=14, unique=True)),
                ('nome', models.CharField(max_length=150)),
                ('apelido', models.CharField(blank=True, max_length=9, null=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('cidade', models.CharField(blank=True, default='Miguel Calmon', max_length=50, null=True)),
                ('complemento', models.CharField(blank=True, max_length=200, null=True)),
                ('batizado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='M', max_length=1)),
                ('data_batismo', models.DateField(null=True, verbose_name='Data de Batismo')),
                ('foto_perfil', models.FileField(blank=True, null=True, upload_to='foto_perfil')),
                ('ativo', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data Cadastro')),
                ('updated', models.DateField(auto_now=True, verbose_name='Data Atualização')),
                ('funcao_lideranca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pessoas.funcaolideranca', verbose_name='Função Liderança')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
