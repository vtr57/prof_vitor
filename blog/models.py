from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings

import os




class NotasAula(models.Model):
    titulo = models.CharField(max_length=255)
    caminho_html = models.CharField(max_length=300)
    slug = models.SlugField(default="", null=False)
    data_criacao = models.DateField(default=timezone.now)
    status_publicado = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(blank=True, null=True)
    
    def criar_arquivo(self, caminho_html):
        caminho_completo = os.path.join(settings.TEMPLATES[0]['DIRS'][0], caminho_html)
        os.makedirs(os.path.dirname(caminho_completo), exist_ok=True)
        if not os.path.exists(caminho_completo):
            with open(caminho_completo, 'w') as f:
                f.write('{% extends "blog/base.html" %}\n{% load static %}\n{% block content %}\n\n{% endblock content %}')
                
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        self.caminho_html = f'blog/posts/{self.slug}.html'
        self.criar_arquivo(self.caminho_html)
        super(NotasAula, self).save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        self.caminho_html = f'blog/posts/{self.slug}.html'
        caminho_completo = os.path.join(settings.TEMPLATES[0]['DIRS'][0], self.caminho_html)
        if os.path.exists(caminho_completo):
            os.remove(caminho_completo)
            super(NotasAula, self).delete(*args, **kwargs)

        
    def publicar(self):
        self.data_publicacao = timezone.now()
        self.status_publicado = True
        self.save()
        
    def __str__(self) -> str:
        return self.caminho_html
        
    class Meta:
        verbose_name = "Nota de Aula"
        verbose_name_plural = "Notas de Aula"

