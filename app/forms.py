from django import forms
from .models import *

# app/forms.py
from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'data_nascimento', 'endereco', 'plano_assinatura']


class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ['nome', 'preco', 'beneficios', 'periodo_teste']
        labels = {
            'periodo_teste': 'Período de Teste (dias)'
        }

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'diretor', 'ano_lancamento', 'genero', 'sinopse', 'elenco', 'duracao']
        widgets = {
            'ano_lancamento': forms.NumberInput(attrs={'min': 1888}),  # O primeiro filme foi em 1888
        }

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['titulo', 'diretor', 'ano_lancamento', 'genero', 'sinopse', 'elenco', 'temporadas', 'episodios']
        widgets = {
            'ano_lancamento': forms.NumberInput(attrs={'min': 1888}),
        }

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['filme', 'nota', 'comentario', 'data_avaliacao', 'usuario']
        widgets = {
            'data_avaliacao': forms.DateInput(attrs={'type': 'date'}),
            'nota': forms.NumberInput(attrs={'min': 0, 'max': 10}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = ['tipo', 'data_geracao', 'conteudo']
        widgets = {
            'data_geracao': forms.DateInput(attrs={'type': 'date'}),
        }

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['usuario', 'data_pagamento', 'valor', 'status']
        widgets = {
            'data_pagamento': forms.DateInput(attrs={'type': 'datetime-local'}),
        }

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ['usuario', 'tipo', 'identificador']

class IdiomaLegendaForm(forms.ModelForm):
    class Meta:
        model = IdiomaLegenda
        fields = ['nome', 'descricao', 'filmes', 'series']

class RedeSocialForm(forms.ModelForm):
    class Meta:
        model = RedeSocial
        fields = ['nome', 'link', 'descricao']

class NotificacaoForm(forms.ModelForm):
    class Meta:
        model = Notificacao
        fields = ['usuario_destinatario', 'tipo', 'conteudo', 'data_envio']
        widgets = {
            'data_envio': forms.DateInput(attrs={'type': 'datetime-local'}),
        }

class RecomendacaoForm(forms.ModelForm):
    class Meta:
        model = Recomendacao
        fields = ['filme', 'descricao', 'data_recomendacao', 'usuario_recomendou']
        widgets = {
            'data_recomendacao': forms.DateInput(attrs={'type': 'datetime-local'}),
        }
        
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']

from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")
    confirmacao_senha = forms.CharField(widget=forms.PasswordInput, label="Confirme a senha")

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'data_nascimento', 'endereco', 'plano_assinatura']  # Não inclua 'senha' aqui

    def clean_confirmacao_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmacao_senha = self.cleaned_data.get('confirmacao_senha')
        if senha and confirmacao_senha and senha != confirmacao_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        return confirmacao_senha

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['senha'])  # Criptografa a senha
        if commit:
            usuario.save()  # Salva o usuário no banco de dados
        return usuario

