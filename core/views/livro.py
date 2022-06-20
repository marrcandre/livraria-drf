from rest_framework.viewsets import ModelViewSet

from core.models import Livro  # Importa o modelo do livro
from core.serializers import LivroSerializer  # Importa o serializer do livro


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
