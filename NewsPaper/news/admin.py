from django.contrib import admin
from .models import Post, Category, Author, PostCategory

# напишем уже знакомую нам функцию обнуления товара на складе
def nullfy_quantity(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(grade=0)
nullfy_quantity.short_description = 'Обнулить рейтинг' # описание для более понятного представления в админ панеле задаётся, как будто это объект


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('title', 'content_choice', 'grade') # генерируем список имён всех полей для более красивого отображения
    list_filter = ('title', 'authors', 'content_choice')
    search_fields = ('title', 'content_choice')
    actions = [nullfy_quantity]  # добавляем действия в список

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(PostCategory)

# Register your models here.
