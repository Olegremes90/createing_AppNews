from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.validators import MinValueValidator
from django.urls import reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('grade'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.user.comment_set.aggregate(commentRating=Sum('grade'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.rating = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return f'{self.user.username}'

class Category(models.Model):
    theme = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User,related_name='categories')

    def __str__(self):
        return self.theme

class Post(models.Model):
    article = 'AR'
    item = 'IT'
    POSITIONS = (
        (article, 'Статья'),
        (item, 'Новость')
    )
    authors = models.ForeignKey('Author', on_delete=models.CASCADE)
    content_choice = models.CharField(max_length=2, choices=POSITIONS, default=item)
    time_creation = models.DateField(auto_now_add=True)
    category = models.ManyToManyField('Category', through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    grade = models.SmallIntegerField(default=0)

    def preview(self):
        return self.text[0:123] + '...'

    def like(self):
        self.grade += 1
        self.save()

    def dislike(self):
        self.grade -= 1
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title




class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category


class Comment(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    time = models.DateField(auto_now_add=True)
    grade = models.SmallIntegerField(default=0)

    def like(self):
        self.grade +=1
        self.save()

    def dislike(self):
        self.grade -=1
        self.save()
    def preview(self):
        return self.text[0:123] + '...'



