from django.db import models
from ckeditor.fields import RichTextField
from apps.profiles.models import Profile


class About(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    ROLES = (
        (0, 'Stuff'),
        (1, 'Manager'),
        (2, 'Founder')
    )
    name = models.CharField(max_length=221)
    avatar = models.ImageField()
    role = models.IntegerField(choices=ROLES)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class History(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField()
    history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HowItWorks(models.Model):
    hiw_num = models.IntegerField()
    hiw_title = models.CharField(max_length=221)

    def __str__(self):
        return self.hiw_title


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


