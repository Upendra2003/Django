from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from user.models import Profile


@receiver(post_save,sender=User)
def createProfile(sender,instance,created,**kwargs):
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            email=user.email,
            name=user.username,
        )


@receiver(post_delete,sender=Profile)
def deleteProfile(sender,instance,**kwargs):
    user=instance.user
    user.delete()


# post_save.connect(profileUpdated,sender=User)
# post_delete.connect(deleteProfile,sender=Profile)