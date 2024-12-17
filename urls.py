from django.contrib import admin
from django.urls import path
from app.views import serve_admin_html  
from django.urls import path
from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView,
    UsuarioListView,
    UsuarioCreateView,
    UsuarioUpdateView,
    UsuarioDeleteView,
    FilmeListView,
    FilmeCreateView,
    FilmeUpdateView,
    FilmeDeleteView,
    SerieListView,
    SerieCreateView,
    SerieUpdateView,
    SerieDeleteView,
    AvaliacaoListView,
    AvaliacaoCreateView,
    AvaliacaoUpdateView,
    AvaliacaoDeleteView,
    CategoriaListView,
    CategoriaCreateView,
    CategoriaUpdateView,
    CategoriaDeleteView,
    RelatorioListView,
    RelatorioCreateView,
    RelatorioUpdateView,
    RelatorioDeleteView,
    Filme1View,  # Certifique-se de que a view Filme1View está importada corretamente
    serve_admin_html,
    ConfiguracaoView,
    CategoriaView,
    payment_view,
    plano_view,
    selecionar_plano,
    plano_view, selecionar_plano,
    login_view, 
    pagina_de_confirmacao,
    user_login,
    
    
  
)
from django.contrib.auth.views import LoginView
from app.views import signup_view, pagina_de_confirmacao
from django import forms
from app.models import Video
from django.conf import settings
from django.conf.urls.static import static
from app import views 
from django.urls import path


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('admin-dashboard/', serve_admin_html, name='admin_dashboard'),  
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/novo/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuarios/<int:pk>/excluir/', UsuarioDeleteView.as_view(), name='usuario_delete'),

    path('filmes/', FilmeListView.as_view(), name='filme_list'),
    path('filmes/novo/', FilmeCreateView.as_view(), name='filme_create'),
    path('filmes/<int:pk>/editar/', FilmeUpdateView.as_view(), name='filme_update'),
    path('filmes/<int:pk>/excluir/', FilmeDeleteView.as_view(), name='filme_delete'),

    path('series/', SerieListView.as_view(), name='serie_list'),
    path('series/novo/', SerieCreateView.as_view(), name='serie_create'),
    path('series/<int:pk>/editar/', SerieUpdateView.as_view(), name='serie_update'),
    path('series/<int:pk>/excluir/', SerieDeleteView.as_view(), name='serie_delete'),

    path('avaliacoes/', AvaliacaoListView.as_view(), name='avaliacao_list'),
    path('avaliacoes/novo/', AvaliacaoCreateView.as_view(), name='avaliacao_create'),
    path('avaliacoes/<int:pk>/editar/', AvaliacaoUpdateView.as_view(), name='avaliacao_update'),
    path('avaliacoes/<int:pk>/excluir/', AvaliacaoDeleteView.as_view(), name='avaliacao_delete'),

    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/novo/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/excluir/', CategoriaDeleteView.as_view(), name='categoria_delete'),

    path('relatorios/', RelatorioListView.as_view(), name='relatorio_list'),
    path('relatorios/novo/', RelatorioCreateView.as_view(), name='relatorio_create'),
    path('relatorios/<int:pk>/editar/', RelatorioUpdateView.as_view(), name='relatorio_update'),
    path('relatorios/<int:pk>/excluir/', RelatorioDeleteView.as_view(), name='relatorio_delete'),

    path('filme1/', Filme1View.as_view(), name='filme1'),  # View Filme1 configurada corretamente
    path('configuracaoes/', ConfiguracaoView.as_view(), name='configuracaoes'), 
    path('configuracao/', ConfiguracaoView.as_view(), name='configuracao'),
    path('categoria/', CategoriaView.as_view(), name='categoria'),  # View Filme1 configurada corretamente


    path('upload/', views.upload_video, name='upload_video'),
    path('videos/', views.video_list, name='video_list'),
    
    path('index/', views.index_view, name='index'),
    path('login/', views.user_login, name='user_login'),  # Página de login # A URL de login
    path('signup/', views.user_signup, name='signup'),  # A URL de cadastro
    
    path('payment/', views.payment_view, name='payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    
    path('plano/', plano_view, name='plano_view'),
    path('selecionar-plano/<int:plano_id>/', selecionar_plano, name='selecionar_plano'),
    path('confirmacao/', pagina_de_confirmacao, name='pagina_de_confirmacao'),
    path('', IndexView.as_view(), name='index'),  # Página principal
    path('criar_perfil/', views.criar_perfil_view, name='criar_perfil'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)