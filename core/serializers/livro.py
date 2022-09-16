from rest_framework.serializers import (CharField, ModelSerializer,
                                        SerializerMethodField,
                                        SlugRelatedField)

from core.models import Livro
from media.models import Image
from media.serializers import ImageSerializer

from .editora import EditoraNestedSerializer


class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Livro
        fields = "__all__"


class LivroDetailSerializer(ModelSerializer):
    categoria = CharField(source="categoria.descricao")
    editora = EditoraNestedSerializer()
    autores = SerializerMethodField()

    capa = ImageSerializer(required=False)

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
