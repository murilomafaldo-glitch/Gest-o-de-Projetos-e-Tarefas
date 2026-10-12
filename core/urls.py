from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_projetos, name='listar_projetos'),
    path('novo/', views.cadastrar_projeto, name='cadastrar_projeto'),
    path('<int:pk>/editar/', views.editar_projeto, name='editar_projeto'),
    path('<int:pk>/excluir/', views.excluir_projeto, name='excluir_projeto'),
]
