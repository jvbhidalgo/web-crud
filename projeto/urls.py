"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app import views
from django.conf.urls import url

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^lista_produto/', views.lista_produto, name='lista_produto'),
    url(r'^novo_produto/', views.novo_produto, name='novo_produto'),
    url(r'^deletar_produto/', views.deletar_produto, name='deletar_produto'),
    url(r'^atualizar_produto/', views.atualizar_produto, name='atualizar_produto'),
    
]