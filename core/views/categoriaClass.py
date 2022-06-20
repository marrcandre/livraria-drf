import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from core.models import Categoria


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
