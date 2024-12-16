from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UsuarioForm, FilmeForm, SerieForm, AvaliacaoForm, CategoriaForm, RelatorioForm, VideoForm
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
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

def payment_view(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    from .models import Usuario, Pagamento, Plano

    usuario = Usuario.objects.get(user=request.user)
    planos = Plano.objects.all()
    if request.method == 'POST':
        plano_id = request.POST.get('plano_id')
        plano = Plano.objects.get(id=plano_id)
        Pagamento.objects.create(
            usuario=usuario,
            plano=plano,
            meio_pagamento=request.POST.get('metodo_pagamento'),
            valor=plano.preco,
            status='pago'
        )
        return redirect('payment_success')
    
    return render(request, 'payment.html', {'planos': planos})

def payment_success(request):
    return render(request, 'payment_success.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class UsuarioListView(View):
    def get(self, request):
        from .models import Usuario
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

class UsuarioUpdateView(View):
    def get(self, request, pk):
        from .models import Usuario
        usuario = get_object_or_404(Usuario, pk=pk)
        form = UsuarioForm(instance=usuario)
        return render(request, 'usuario_form.html', {'form': form})

    def post(self, request, pk):
        from .models import Usuario
        usuario = get_object_or_404(Usuario, pk=pk)
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
        return render(request, 'usuario_form.html', {'form': form})

class UsuarioDeleteView(View):
    def post(self, request, pk):
        from .models import Usuario
        usuario = Usuario.objects.get(pk=pk)
        usuario.delete()
        return redirect('usuario_list')

class FilmeListView(View):
    def get(self, request):
        from .models import Filme
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
        from .models import Filme
        filme = Filme.objects.get(pk=pk)
        form = FilmeForm(instance=filme)
        return render(request, 'filme_form.html', {'form': form})

    def post(self, request, pk):
        from .models import Filme
        filme = Filme.objects.get(pk=pk)
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('filme_list')
        return render(request, 'filme_form.html', {'form': form})

class FilmeDeleteView(View):
    def post(self, request, pk):
        from .models import Filme
        filme = Filme.objects.get(pk=pk)
        filme.delete()
        return redirect('filme_list')

class SerieListView(View):
    def get(self, request):
        from .models import Serie
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
        from .models import Serie
        serie = Serie.objects.get(pk=pk)
        form = SerieForm(instance=serie)
        return render(request, 'serie_form.html', {'form': form})

    def post(self, request, pk):
        from .models import Serie
        serie = Serie.objects.get(pk=pk)
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
            return redirect('serie_list')
        return render(request, 'serie_form.html', {'form': form})

class SerieDeleteView(View):
    def post(self, request, pk):
        from .models import Serie
        serie = Serie.objects.get(pk=pk)
        serie.delete()
        return redirect('serie_list')

class AvaliacaoListView(View):
    def get(self, request):
        from .models import Avaliacao
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
        from .models import Avaliacao
        avaliacao = Avaliacao.objects.get(pk=pk)
        form = AvaliacaoForm(instance=avaliacao)
        return render(request, 'avaliacao_form.html', {'form': form})

    def post(self, request, pk):
        from .models import Avaliacao
        avaliacao = Avaliacao.objects.get(pk=pk)
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('avaliacao_list')
        return render(request, 'avaliacao_form.html', {'form': form})

class AvaliacaoDeleteView(View):
    def post(self, request, pk):
        from .models import Avaliacao
        avaliacao = Avaliacao.objects.get(pk=pk)
        avaliacao.delete()
        return redirect('avaliacao_list')

class CategoriaListView(View):
    def get(self, request):
        from .models import Categoria
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
        from .models import Categoria
        categoria = Categoria.objects.get(pk=pk)
        form = CategoriaForm(instance=categoria)
        return render(request, 'categoria_form.html', {'form': form})

    def post(self, request, pk):
        from .models import Categoria
        categoria = Categoria.objects.get(pk=pk)
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
        return render(request, 'categoria_form.html', {'form': form})

class CategoriaDeleteView(View):
    def post(self, request, pk):
        from .models import Categoria
        categoria = Categoria.objects.get(pk=pk)
        categoria.delete()
        return redirect('categoria_list')

class RelatorioListView(View):
    def get(self, request):
        from .models import Relatorio
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
        from .models import Relatorio
        relatorio = Relatorio.objects.get(pk=pk)
        form = RelatorioForm(instance=relatorio)
        return render(request, 'relatorio_form.html', {'form': form})

    def post(self, request, pk):
        from .models import Relatorio
        relatorio = Relatorio.objects.get(pk=pk)
        form = RelatorioForm(request.POST, instance=relatorio)
        if form.is_valid():
            form.save()
            return redirect('relatorio_list')
        return render(request, 'relatorio_form.html', {'form': form})

class RelatorioDeleteView(View):
    def post(self, request, pk):
        from .models import Relatorio
        relatorio = Relatorio.objects.get(pk=pk)
        relatorio.delete()
        return redirect('relatorio_list')

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_video')
    else:
        form = VideoForm()
    
    return render(request, 'upload_video.html', {'form': form})

def video_list(request):
    from .models import Video
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def plano_view(request):
    from .models import Plano
    planos = Plano.objects.all()[:3]
    return render(request, 'plano.html', {'planos': planos})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            plano_id = request.session.get('plano_selecionado')
            if plano_id:
                return redirect('pagina_de_confirmacao')
            else:
                return redirect('pagina_inicial')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

class CategoriaView(View):
    def get(self, request):
        return render(request, 'categoria.html')

class ConfiguracaoView(View):
    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        from .models import Usuario
        usuario = get_object_or_404(Usuario, user=request.user)
        return render(request, 'configuracoes.html', {'usuario': usuario})

    @method_decorator(login_required, name='dispatch')
    def post(self, request):
        from .models import Usuario
        usuario = get_object_or_404(Usuario, user=request.user)
        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.data_nascimento = request.POST.get('data_nascimento')
        usuario.endereco = request.POST.get('endereco')
        usuario.plano_assinatura = request.POST.get('plano_assinatura')
        usuario.save()
        return redirect('configuracao')

def selecionar_plano(request, plano_id):
    from .models import Plano
    try:
        plano = Plano.objects.get(id=plano_id)
        request.session['plano_selecionado'] = plano.id
        if request.user.is_authenticated:
            return redirect('pagina_de_confirmacao')
        else:
            return redirect('user_login')
    except Plano.DoesNotExist:
        return redirect('plano_view')

def pagina_de_confirmacao(request):
    from .models import Plano
    plano_id = request.session.get('plano_selecionado')
    
    if plano_id:
        try:
            plano = Plano.objects.get(id=plano_id)
            return render(request, 'confirmacao_plano.html', {'plano': plano})
        except Plano.DoesNotExist:
            return redirect('plano_view')
    else:
        return redirect('plano_view')