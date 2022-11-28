from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponse


class PostsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'
    pyginate_by=2
# Create your views here.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        return context



class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'flatpages/post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'

def multiply(request):
        number = request.GET.get('number')
        multiplier = request.GET.get('multiplier')

        try:
           result = int(number) * int(multiplier)
           html = f"<html><body>{number}*{multiplier}={result}</body></html>"
        except (ValueError, TypeError):
           html = f"<html><body>Invalid input.</body></html>"

        return HttpResponse(html)