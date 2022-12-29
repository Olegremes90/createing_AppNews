from celery import shared_task
import time
import datetime
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import *


@shared_task
def send_notifications(preview, pk, title, subscribers):
    mailing_list = list(PostCategory.objects.filter(postThrough_id=pk).values_list(
        'categoryThrough__subscribers__username',
        'categoryThrough__subscribers__first_name',
        'categoryThrough__subscribers__email',
        'categoryThrough__name',
        )
    )
    for user, first_name, email, category in mailing_list:
        if not first_name:
            first_name = user
    html_content= render_to_string(
        'post_created_email.html',
        {
            'name': first_name,
            'category': category,
            'title': title,
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}',

        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def every_monday_notify():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days = 7)
    posts = Post.objects.filter(time_creation__gte=last_week)
    categories = set(posts.values_list('category__theme', flat=True))
    subscribers = set(Category.objects.filter(theme__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()