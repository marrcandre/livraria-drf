from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from core.models import Autor, Categoria, Compra, Editora, ItensCompra, Livro


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"


class EditoraNestedSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = ("nome",)


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class LivroDetailSerializer(ModelSerializer):
    categoria = CharField(source="categoria.descricao")
    editora = EditoraNestedSerializer()
    autores = SerializerMethodField()

    def get_autores(self, instance):
        # nomes_autores = []
        # autores = instance.autores.get_queryset()
        # for autor in autores:
        #     nomes_autores.append(autor.nome)
        # return nomes_autores
        return [autor.nome for autor in instance.autores.get_queryset()]

    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("quantidade", "total", "livro")
        depth = 2


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email")
    status = CharField(source="get_status_display")
    itens = ItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
