from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    plano_assinatura = models.CharField(max_length=50)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    plano_assinatura = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

class Plano(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    beneficios = models.TextField()
    periodo_teste = models.IntegerField()  # em dias

    class Meta:
        verbose_name = 'Planos'

class Pagamento(models.Model):
    VALOR_CHOICES = [
        ('9.90', 'R$ 9,90'),
        ('19.90', 'R$ 19,90'),
        ('47.75', 'R$ 47,75'),
    ]
    meio_pagamento = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_pagamento = models.DateTimeField(default=timezone.now)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    valor = models.CharField(max_length=10, choices=VALOR_CHOICES)
    status = models.CharField(max_length=20, choices=(('pago', 'Pago'), ('pendente', 'Pendente')))

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['-data_pagamento']

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    diretor = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    genero = models.ManyToManyField('Categoria', related_name='filmes')
    sinopse = models.TextField()
    elenco = models.TextField()
    duracao = models.IntegerField()  # em minutos

    class Meta:
        verbose_name = 'Filmes'

class Serie(models.Model):
    titulo = models.CharField(max_length=200)
    diretor = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    genero = models.ManyToManyField('Categoria', related_name='series')
    sinopse = models.TextField()
    elenco = models.TextField()
    temporadas = models.IntegerField()
    episodios = models.IntegerField()

    class Meta:
        verbose_name = 'Series'

class Avaliacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField()

    class Meta:
        verbose_name = 'Avaliacao'

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categoria'

class Relatorio(models.Model):
    tipo = models.CharField(max_length=100)
    data_geracao = models.DateTimeField()
    conteudo = models.TextField()

    class Meta:
        verbose_name = 'Relatorio'

class Dispositivo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    identificador = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Dispositivo'

class IdiomaLegenda(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    filmes = models.ManyToManyField(Filme)
    series = models.ManyToManyField(Serie)

    class Meta:
        verbose_name = 'IdiomaLegenda'

class RedeSocial(models.Model):
    nome = models.CharField(max_length=100)
    link = models.URLField()
    descricao = models.TextField()

    class Meta:
        verbose_name = 'RedeSocial'

class Notificacao(models.Model):
    usuario_destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_envio = models.DateTimeField()

    class Meta:
        verbose_name = 'Notificacao'

class Recomendacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_recomendacao = models.DateTimeField()
    usuario_recomendou = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Recomendacao'

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')

    class Meta:
        verbose_name = 'Video'