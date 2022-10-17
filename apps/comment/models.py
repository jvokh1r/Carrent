from django.db import models
from apps.profiles.models import Profile
from apps.blog.models import Article


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name

