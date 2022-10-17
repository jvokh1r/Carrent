from django.db import models


class Service(models.Model):
    icon = models.ImageField()
    title = models.CharField(max_length=221)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
