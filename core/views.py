from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Categoria

import json


def teste(request):
    return HttpResponse("<h1>Olá Mundo do Django</h1>")


def teste2(request):
    return HttpResponse("<h1>Uma nova página</h1>")


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):
    model = Categoria

    def get(self, request, id=None):
        if id:
            qs = Categoria.objects.get(id=id)
            data = {"id": qs.id, "descricao": qs.descricao}
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)

        return JsonResponse(data, safe=False)

    def post(self, request):
        json_data = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**json_data)
        data = {"id": nova_categoria.id, "descricao": nova_categoria.descricao}
        return JsonResponse(data)


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class CategoriasList(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaDetail(APIView):
    def get(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    def put(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        print(serializer)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

