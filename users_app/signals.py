from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to Movie Review Site!',
            'Hi there, thanks for registering!',
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=True
        )