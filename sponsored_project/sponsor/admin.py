from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.City)
admin.site.register(models.Event)
admin.site.register(models.EventDetails)
admin.site.register(models.Category)
admin.site.register(models.Sponsor)
admin.site.register(models.Organiser)