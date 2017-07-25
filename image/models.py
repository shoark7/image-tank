from django.conf import settings
from django.db import models


class Image(models.Model):
    likes = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to='')
    uploaded_date = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo.name
