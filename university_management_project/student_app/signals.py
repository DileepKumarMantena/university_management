from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Faculty

@receiver(post_save, sender=Faculty)
def faculty_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"A new faculty member has been registered: {instance}")

@receiver(post_delete, sender=Faculty)
def faculty_post_delete(sender, instance, **kwargs):
    print(f"Faculty member has been deleted: {instance}")
