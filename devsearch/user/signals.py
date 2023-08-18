from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from user.models import Profile
from django.shortcuts import redirect
from django.urls import reverse


@receiver(post_save,sender=User)
def createProfile(sender,instance,created,**kwargs):
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            email=user.email,
            name=user.username,
        )

@receiver(post_save,sender=Profile)
def updateProfile(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created==False:
        user.first_name=profile.name
        user.email=profile.email
        user.save()


@receiver(post_delete,sender=Profile)
def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()

# post_save.connect(profileUpdated,sender=User)
# post_delete.connect(deleteProfile,sender=Profile)