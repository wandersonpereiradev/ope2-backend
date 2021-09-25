"""managementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from produtos.api import viewsets as produtosviewsets
from compras.api import viewsets as comprasviewsets
from usuarios.api import viewsets as usuariosviewsets
from servicos.api import viewsets as servicosviewsets

route = routers.DefaultRouter()

route.register(r'produtos', produtosviewsets.ProdutosViewSets, basename = 'Produtos')
route.register(r'compras', comprasviewsets.ComprasViewSets, basename = 'Compras')
route.register(r'usuarios', usuariosviewsets.UsuariosViewSets, basename = 'Usuarios')
route.register(r'servicos', servicosviewsets.ServicosViewSets, basename = 'Servicos')

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),

    # user management allauth
    path('accounts/', include("allauth.urls")),

    # user management JWT
    #path('token/', TokenObtainPairView.as_view()),
    #path('token/refresh/', TokenRefreshView.as_view()),

    #local
    path('', include(route.urls)),
]
