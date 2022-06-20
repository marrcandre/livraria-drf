from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register(r'autores',  views.AutorViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'compras', views.CompraViewSet)
router.register(r'editoras', views.EditoraViewSet)
router.register(r'livros', views.LivroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("teste/", views.teste),
    path("pag2/", views.teste2),
    path("categorias-class/", views.CategoryView.as_view()),
    path("categorias-class/<int:id>/", views.CategoryView.as_view()),
    path("categorias-apiview/", views.CategoriasList.as_view()),
    path("categorias-apiview/<int:id>/", views.CategoriaDetail.as_view()),
    path("categorias-generic/", views.CategoriasListGeneric.as_view()),
    path("categorias-generic/<int:id>/", views.CategoriaDetailGeneric.as_view()),
    path('', include(router.urls)),
]
