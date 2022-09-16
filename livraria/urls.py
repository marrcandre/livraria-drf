from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import (
    AutorViewSet,
    CategoriaViewSet,
    CompraViewSet,
    EditoraViewSet,
    LivroViewSet,
)
from media.router import router as media_router

router = DefaultRouter()
router.register(r"autores", AutorViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"compras", CompraViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"livros", LivroViewSet)

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
    path("api/media/", include(media_router.urls)),
    path("", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
