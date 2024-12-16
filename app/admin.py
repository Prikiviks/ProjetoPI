from django.contrib import admin
from .models import *  # Certifique-se de que isso está importando seu modelo corretamente

admin.site.register(Usuario)
admin.site.register(Plano)
admin.site.register(Pagamento)
admin.site.register(Filme)
admin.site.register(Serie)
admin.site.register(Avaliacao)
admin.site.register(Categoria)
admin.site.register(Relatorio)
admin.site.register(Dispositivo)
admin.site.register(IdiomaLegenda)
admin.site.register(RedeSocial)
admin.site.register(Notificacao)
admin.site.register(Recomendacao)
admin.site.register(Video)


