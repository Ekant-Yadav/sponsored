from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

# Imports for extending User model

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(User):
    # Add city field to the User model

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    city = models.CharField(max_length=50)


'''# Create the Sponsor instance when User is saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save the user
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

'''


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = UserProfile(user=user)
        profile.save()


class City(models.Model):
    name = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(2, 'City name should have at least 2 characters')]
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(2, 'Category title should have at least 2 characters')]
    )
    events = models.ManyToManyField('Event', through='EventDetails')

    def __str__(self):
        return self.category


class Sponsor(models.Model):
    name = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(2, 'Name should have at least 2 characters')]
    )
    events = models.ManyToManyField('Event', through='EventDetails')

    def __str__(self):
        return self.name


class Organiser(models.Model):
    name = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(2, 'Category title should have at least 2 characters')]
    )
    events = models.ManyToManyField('Event', through='EventDetails')

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(2, 'Title should have at least 2 Characters')]
    )

    def __str__(self):
        return self.title


class EventDetails(models.Model):
    title = models.ForeignKey(Event, on_delete=models.CASCADE)
    description = models.TextField()
    event_date = models.DateTimeField()

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    organisers = models.ForeignKey(Organiser, on_delete=models.CASCADE)
    sponsors = models.ForeignKey(Sponsor, on_delete=models.SET_NULL, null=True)
