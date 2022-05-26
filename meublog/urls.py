from django.urls import path

from . import views

app_name = 'meublog'

urlpatterns = [
    path('', views.ListarPostsView.as_view(), name='listar_posts'),
    path('<int:ano>/<int:mes>/<int:dia>/<slug:slug>/',
         views.DetalharPostView.as_view(), name='detalhe'),
    path('enviarpost/<int:pk>/',
         views.FormContatoView.as_view(),
         name='enviarpost'),
    path('comentar/<int:pk>/',
         views.ComentarioCreateView.as_view(),
         name='comentar_post'),
    path('cadastrousuario/',
         views.CadUsuarioView.as_view(),
         name="cadastrouser"),
    path('login/', views.LoginUsuarioView.as_view(),
         name='loginuser'),
    path('logout/', views.LogoutUsuarioView.as_view(),
         name='logoutuser')
]
