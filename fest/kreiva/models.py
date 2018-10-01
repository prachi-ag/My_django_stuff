from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username


class UserPartiInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_participated")
    event = models.CharField(max_length=200)

    def __str__(self):
        return self.event
