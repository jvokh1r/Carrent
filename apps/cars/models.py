from django.db import models


class Cars(models.Model):
    TRANS = (
        ('None', 'None'),
        ('Mechanic', 'Mechanic'),
        ('Automatic', 'Automatic'),
        ('AI', 'AI')
    )
    PRICE = (
        ('$', '$'),
        ('Euro', 'Euro'),
    )
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='media/')
    price = models.IntegerField()
    price_value = models.CharField(max_length=50, choices=PRICE, default='$')
    doors = models.IntegerField()
    seats = models.IntegerField()
    trans = models.CharField(max_length=50, choices=TRANS, default='None')
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    where_from = models.CharField(max_length=221)
    where_to = models.CharField(max_length=221)
    go_date = models.DateTimeField()
    back_date = models.DateTimeField()
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.where_to



