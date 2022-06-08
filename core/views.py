from django.http import HttpResponse

def teste(request):
    return HttpResponse("<h1>Olá Mundo do Django</h1>")

def teste2(request):
    return HttpResponse("<h1>Uma nova página</h1>")