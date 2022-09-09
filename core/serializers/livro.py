from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CharField, SerializerMethodField

from core.models import Livro
from .editora import EditoraNestedSerializer

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