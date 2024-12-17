
from django.views.generic import TemplateView 
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from app.models import *
from app.forms import (
    UsuarioForm,
    FilmeForm,
    SerieForm,
    AvaliacaoForm,
    CategoriaForm,
    RelatorioForm,
)

from django.views import View


# Remova ou comente esta linha
# from app.views import IndexView  # ou qualquer outra view que você tenha

# myapp/views.py

from django.shortcuts import render

def serve_admin_html(request):
    return render(request, 'admin.html')



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Usuario


@login_required
def configuracao_view(request):
    try:
        usuario = request.user.usuario  # Acessando o perfil do usuário relacionado
    except Usuario.DoesNotExist:
        usuario = None

    if request.method == 'POST':
        # Atualizando informações do perfil
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')
        endereco = request.POST.get('endereco')
        plano_assinatura = request.POST.get('plano_assinatura')

        if usuario:
            usuario.nome = nome
            usuario.email = email
            usuario.data_nascimento = data_nascimento
            usuario.endereco = endereco
            usuario.plano_assinatura = plano_assinatura
            usuario.save()

        # Redireciona após a atualização
        return redirect('configuracao')

    return render(request, 'configuracao.html', {'usuario': usuario})


#VIEWWS FILMES LISTAS
class Filme1View(TemplateView):
    template_name = 'filme1.html'


from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Usuario



from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Usuario

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

class IndexView(TemplateView):
    template_name = 'index.html'


# Continue with other views...
import json
from django.utils.decorators import method_decorator

class IndexView(TemplateView):
    template_name = 'index.html'

def serve_admin_html(request):
    return render(request, 'admin.html')



class Filme1View(TemplateView):
    template_name = 'filme1.html'

@login_required
def index_view(request):
    is_user_logged_in = request.user.is_authenticated
    return render(request, 'index.html', {'user_logged_in': is_user_logged_in})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')  # Agora usa o email
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)  # Busca o usuário pelo email
        except User.DoesNotExist:
            user = None
        
        if user is not None:
            user = authenticate(request, username=user.username, password=password)  # Verifica a senha
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'registration/login.html', {'error': 'Credenciais inválidas'})
        else:
            return render(request, 'registration/login.html', {'error': 'Credenciais inválidas'})
    
    return render(request, 'registration/login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 and password2 and password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'signup.html', {'error': 'Preencha todos os campos corretamente.'})
    return render(request, 'signup.html')

@login_required
def index_view(request):
    return render(request, 'index.html', {'user_logged_in': request.user.is_authenticated})

@login_required
def index_view(request):
    return render(request, 'index.html', {'user_logged_in': request.user.is_authenticated})

def payment_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Se o usuário não está autenticado, redireciona para o login

    usuario = Usuario.objects.get(user=request.user)
    planos = Plano.objects.all()  # Exibe os planos disponíveis
    if request.method == 'POST':
        # Aqui você pode processar o pagamento
        plano_id = request.POST.get('plano_id')
        plano = Plano.objects.get(id=plano_id)
        
        # Simula o pagamento
        pagamento = Pagamento.objects.create(
            usuario=usuario,
            plano=plano,
            meio_pagamento=request.POST.get('metodo_pagamento'),
            valor=plano.preco,  # Aqui você pode capturar o valor real dependendo do plano
            status='pago'  # Marca o pagamento como 'pago'
        )
        # Redireciona para a página de sucesso
        return redirect('payment_success')
    
    return render(request, 'payment.html', {'planos': planos})

def payment_success(request):
    return render(request, 'payment_success.html')




from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o cadastro
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

      
# VIEWS USUARIO
class UsuarioListView(View):
    def get(self, request):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario_list.html', {'usuarios': usuarios})

class UsuarioCreateView(View):
    def get(self, request):
        form = UsuarioForm()
        return render(request, 'usuario_form.html', {'form': form})

    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
        return render(request, 'usuario_form.html', {'form': form})

from django.shortcuts import get_object_or_404

class UsuarioUpdateView(View):
    def get(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        form = UsuarioForm(instance=usuario)
        return render(request, 'usuario_form.html', {'form': form})

    def post(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
        return render(request, 'usuario_form.html', {'form': form})

class UsuarioDeleteView(View):
    def post(self, request, pk):
        usuario = Usuario.objects.get(pk=pk)
        usuario.delete()
        return redirect('usuario_list')

# VIEWS FILME
class FilmeListView(View):
    def get(self, request):
        filmes = Filme.objects.all()
        return render(request, 'filme_list.html', {'filmes': filmes})

class FilmeCreateView(View):
    def get(self, request):
        form = FilmeForm()
        return render(request, 'filme_form.html', {'form': form})

    def post(self, request):
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filme_list')
        return render(request, 'filme_form.html', {'form': form})

class FilmeUpdateView(View):
    def get(self, request, pk):
        filme = Filme.objects.get(pk=pk)
        form = FilmeForm(instance=filme)
        return render(request, 'filme_form.html', {'form': form})

    def post(self, request, pk):
        filme = Filme.objects.get(pk=pk)
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('filme_list')
        return render(request, 'filme_form.html', {'form': form})

class FilmeDeleteView(View):
    def post(self, request, pk):
        filme = Filme.objects.get(pk=pk)
        filme.delete()
        return redirect('filme_list')

# VIEWS SERIE

class SerieListView(View):
    def get(self, request):
        series = Serie.objects.all()
        return render(request, 'serie_list.html', {'series': series})

class SerieCreateView(View):
    def get(self, request):
        form = SerieForm()
        return render(request, 'serie_form.html', {'form': form})

    def post(self, request):
        form = SerieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('serie_list')
        return render(request, 'serie_form.html', {'form': form})

class SerieUpdateView(View):
    def get(self, request, pk):
        serie = Serie.objects.get(pk=pk)
        form = SerieForm(instance=serie)
        return render(request, 'serie_form.html', {'form': form})

    def post(self, request, pk):
        serie = Serie.objects.get(pk=pk)
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
            return redirect('serie_list')
        return render(request, 'serie_form.html', {'form': form})

class SerieDeleteView(View):
    def post(self, request, pk):
        serie = Serie.objects.get(pk=pk)
        serie.delete()
        return redirect('serie_list')
    
# app/views.py

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'


# VIEWS AVALIACAO
class AvaliacaoListView(View):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao_list.html', {'avaliacoes': avaliacoes})

class AvaliacaoCreateView(View):
    def get(self, request):
        form = AvaliacaoForm()
        return render(request, 'avaliacao_form.html', {'form': form})

    def post(self, request):
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('avaliacao_list')
        return render(request, 'avaliacao_form.html', {'form': form})

class AvaliacaoUpdateView(View):
    def get(self, request, pk):
        avaliacao = Avaliacao.objects.get(pk=pk)
        form = AvaliacaoForm(instance=avaliacao)
        return render(request, 'avaliacao_form.html', {'form': form})

    def post(self, request, pk):
        avaliacao = Avaliacao.objects.get(pk=pk)
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('avaliacao_list')
        return render(request, 'avaliacao_form.html', {'form': form})

class AvaliacaoDeleteView(View):
    def post(self, request, pk):
        avaliacao = Avaliacao.objects.get(pk=pk)
        avaliacao.delete()
        return redirect('avaliacao_list')

# VIEWS CATEGORIA
class ConfiguracaoView(View):
    def get(self, request):
        return render(request,'configuracoes.html',)
class CategoriaView(View):
    def get(self, request):
        return render(request,'categoria.html',)
        
        
class CategoriaListView(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, 'categoria_list.html', {'categorias': categorias})

class CategoriaCreateView(View):
    def get(self, request):
        form = CategoriaForm()
        return render(request, 'categoria_form.html', {'form': form})

    def post(self, request):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
        return render(request, 'categoria_form.html', {'form': form})

class CategoriaUpdateView(View):
    def get(self, request, pk):
        categoria = Categoria.objects.get(pk=pk)
        form = CategoriaForm(instance=categoria)
        return render(request, 'categoria_form.html', {'form': form})

    def post(self, request, pk):
        categoria = Categoria.objects.get(pk=pk)
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
        return render(request, 'categoria_form.html', {'form': form})

class CategoriaDeleteView(View):
    def post(self, request, pk):
        categoria = Categoria.objects.get(pk=pk)
        categoria.delete()
        return redirect('categoria_list')

# VIEWS RELATORIO
class RelatorioListView(View):
    def get(self, request):
        relatorios = Relatorio.objects.all()
        return render(request, 'relatorio_list.html', {'relatorios': relatorios})

class RelatorioCreateView(View):
    def get(self, request):
        form = RelatorioForm()
        return render(request, 'relatorio_form.html', {'form': form})

    def post(self, request):
        form = RelatorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relatorio_list')
        return render(request, 'relatorio_form.html', {'form': form})

class RelatorioUpdateView(View):
    def get(self, request, pk):
        relatorio = Relatorio.objects.get(pk=pk)
        form = RelatorioForm(instance=relatorio)
        return render(request, 'relatorio_form.html', {'form': form})

    def post(self, request, pk):
        relatorio = Relatorio.objects.get(pk=pk)
        form = RelatorioForm(request.POST, instance=relatorio)
        if form.is_valid():
            form.save()
            return redirect('relatorio_list')
        return render(request, 'relatorio_form.html', {'form': form})

class RelatorioDeleteView(View):
    def post(self, request, pk):
        relatorio = Relatorio.objects.get(pk=pk)
        relatorio.delete()
        return redirect('relatorio_list')


from django.shortcuts import render, redirect
from .forms import VideoForm

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_video')  # Ou outra página
    else:
        form = VideoForm()
    
    return render(request, 'upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})
#PAGAMENTO
def payment_view(request):
    return render(request, 'payment.html')

def plano_view(request):
    planos = Plano.objects.all()[:3]  # Apenas 3 planos serão mostrados do banco
    return render(request, 'plano.html', {'planos': planos})
# views.py
from django.shortcuts import render, redirect
from .models import Plano

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Verifica se há um plano selecionado na sessão
            plano_id = request.session.get('plano_selecionado')
            if plano_id:
                return redirect('pagina_de_confirmacao')  # Redireciona para a página de confirmação do plano
            else:
                return redirect('pagina_inicial')  # Ou redirecione para a página inicial caso o plano não esteja mais disponível
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Plano

def selecionar_plano(request, plano_id):
    try:
        plano = Plano.objects.get(id=plano_id)
        # Armazena o ID do plano selecionado na sessão
        request.session['plano_selecionado'] = plano.id
        
        # Verifica se o usuário está autenticado
        if request.user.is_authenticated:
            # Se o usuário estiver autenticado, redireciona para a página de confirmação
            return redirect('pagina_de_confirmacao')
        else:
            # Se o usuário não estiver autenticado, redireciona para a página de login
            return redirect('login')  # Ou para a página de criação de conta, se necessário
    except Plano.DoesNotExist:
        # Se o plano não for encontrado, redireciona para a página de planos
        return redirect('plano_view')
    
from django.shortcuts import render
from .models import Plano

def pagina_de_confirmacao(request):
    plano_id = request.session.get('plano_selecionado')  # Obtém o ID do plano da sessão
    
    if plano_id:
        try:
            # Recupera o objeto Plano do banco de dados
            plano = Plano.objects.get(id=plano_id)
            return render(request, 'confirmacao_plano.html', {'plano': plano})
        except Plano.DoesNotExist:
            # Se o plano não for encontrado no banco de dados
            return redirect('plano_view')
    else:
        # Se não houver plano selecionado na sessão, redireciona para a página inicial
        return redirect('plano_view')



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Usuario
from .forms import EditarPerfilForm
@login_required
def configuracao_view(request):
    try:
        usuario = request.user.usuario  # Acessando o perfil do usuário
    except Usuario.DoesNotExist:
        # Caso o perfil não exista, você pode redirecionar para uma página onde o usuário possa criar o perfil
        return redirect('criar_perfil')  # Redireciona para a página de criação do perfil

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('configuracao')  # Redireciona após salvar as alterações
    else:
        form = EditarPerfilForm(instance=usuario)

    return render(request, 'configuracoes.html', {'form': form, 'usuario': usuario})

@login_required
def criar_perfil_view(request):
    if request.method == 'POST':
        # Criando um novo perfil para o usuário logado
        usuario = Usuario(user=request.user)
        usuario.save()
        return redirect('configuracao')  # Redireciona para a página de configuração
    return render(request, 'criar_perfil.html')

