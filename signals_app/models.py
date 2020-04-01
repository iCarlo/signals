from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.first_name


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile Created!")

post_save.connect(create_profile, sender=User)


def update_profile(sender, instance, created, **kwargs):
    if created is False:
        instance.profile.save()
        print("Profile Updated!")

post_save.connect(update_profile, sender=User)
