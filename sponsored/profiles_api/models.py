from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Add city field to the User model

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='+')
    location = models.CharField(max_length=50)
    profile = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
# def save_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = UserProfile(user=user)
#         profile.save()
