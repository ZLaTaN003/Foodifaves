from django.contrib.auth.models import User
from . models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save,sender=User)
def build_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)



def save_profile(sender,instance,**kwargs):
    instance.profile.save()