from django.db import models


class FeedBack(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='feedback')
    msg = models.TextField()

    def __str__(self):
        return self.name
