from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


from .models import NotasAula

def index(request):
    notas_publicadas = NotasAula.objects.filter(status_publicado=True).order_by('-data_publicacao')
    context = {
        'notas_publicadas': notas_publicadas,
    }
    return render(request, 'blog/index.html', context)

def detalhes_notas(request, slug):
    nota = get_object_or_404(NotasAula, slug=slug, status_publicado=True)
    context = {
        'nota': nota
    }
    return render(request, f'blog/posts/{nota.slug}.html')

def sobre(request):
    return render(request, 'blog/sobre.html')

def contato(request):
    return HttpResponse("Contato    ")
