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

from core.views import teste, teste2, CategoryView, CategoriasList, CategoriaDetail, CategoriasListGeneric, CategoriaDetailGeneric
from media.router import router as media_router

router = DefaultRouter()
router.register(r"autores", AutorViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"compras", CompraViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"livros", LivroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("teste/", teste),
    path("pag2/", teste2),
    path("categorias-class/", CategoryView.as_view()),
    path("categorias-class/<int:id>/", CategoryView.as_view()),
    path("categorias-apiview/", CategoriasList.as_view()),
    path("categorias-apiview/<int:id>/", CategoriaDetail.as_view()),
    path("categorias-generic/", CategoriasListGeneric.as_view()),
    path("categorias-generic/<int:id>/", CategoriaDetailGeneric.as_view()),
    path("api/media/", include(media_router.urls)),
    path("", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
