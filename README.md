Blog com aulas de Física, para divulgação da Física e do Ensino de Física.

## Criar uma nota de aula

Vá até a página de admin e adicione a nota de aula.
Isso irá criar um template no caminho `blog/templates/blog/posts/{notas.slug}.html`.
O arquivo html deve se preenchido internamente a tag `<div class="content">`.

### Padrão de criação do template

| Estrutura de texto | Tag |
| --------|------|
| Título da nota de aula | `h1` |
| Introdução da nota de aula | `<p class="introducao">` |
| Parágrafos | `p` |
| Subtítulos | `h2` |
| listas nã ordenadas | `ol`|
| Exemplos | `<div class="exemplo">` |
| Resolução dos exemplos | `<div class="exemplo"><div class="resolucao">` |
| Dados dos exemplos | `<div class="exemplo"><div class="resolucao"><div class="dados">`|
| Exercícios | `<div class="exercicios">` |
| Enunciado exercício | `<ol class="enunciado">`|
| Opções dos exercícios | `<ol class="enunciado"><ol class="opcoes">`|
| link para outra nota | `<a href="{% url 'nota' slug='{nota.slug}' %}">` |
| vídeo YouTube | `<div class="container-video-youtube"><iframe class="video-youtube" src="" title="" frameborder="0" allow="" referrerpolicy="" allowfullscreen>`|
