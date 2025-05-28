from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movie

@receiver(post_save, sender=Movie)
def log_movie_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New movie added: {instance.title}")

        

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Movie

@receiver(post_save, sender=Movie)
def notify_admin_on_new_movie(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='🎬 New Movie Added',
            message=f"A new movie has been added: {instance.title}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['your_email@example.com'],  # ← აქ ჩაწერე შენი ელფოსტა
            fail_silently=True
        )