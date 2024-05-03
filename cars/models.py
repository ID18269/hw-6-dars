from django.db import models


class CarModel(models.Model):
    image = models.ImageField(upload_to='cars-images', null=True)
    company = models.CharField(max_length=128)
    model = models.CharField(max_length=255)
    info = models.TextField()
    speed = models.IntegerField()
    price = models.SmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'
