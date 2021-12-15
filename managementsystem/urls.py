from managementsystem.settings import TEMPLATES
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from produtos.api import viewsets as produtosviewsets
from compras.api import viewsets as comprasviewsets
from usuarios.api import viewsets as usuariosviewsets
from servicos.api import viewsets as servicosviewsets
from clientes.api import viewsets as clientesviewsets

route = routers.DefaultRouter()

route.register(r'produtos', produtosviewsets.ProdutosViewSets, basename = 'Produtos')
route.register(r'compras', comprasviewsets.ComprasViewSets, basename = 'Compras')
route.register(r'usuarios', usuariosviewsets.UsuariosViewSets, basename = 'Usuarios')
route.register(r'servicos', servicosviewsets.ServicosViewSets, basename = 'Servicos')
route.register(r'clientes', clientesviewsets.ClientesViewSets, basename = 'Clientes')

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),


    # user management JWT
    #path('token/', TokenObtainPairView.as_view()),
    #path('token/refresh/', TokenRefreshView.as_view()),

    #local
    path('sistema/', include(route.urls)),
    path("", include("pages.urls", namespace="pages")),

    # user management allauth
    path('accounts/', include("allauth.urls")),
]
