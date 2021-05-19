from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    phone = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Currency(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return str(self.owner)

    def get_absolute_url(self):
        return reverse('home')