from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from .models import PostCategory, Post
from .tasks import send_notifications




@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
             subscribers += category.subscribers.all()
             print(subscribers)
             subscribers = [s.email for s in subscribers]



             send_notifications.apply_async(
                     (instance.preview(), instance.pk, instance.title, subscribers),
                     countdown= 10
             )


