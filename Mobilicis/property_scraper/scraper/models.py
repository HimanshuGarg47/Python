from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=50)
    property_type = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    property_link = models.URLField()

    def __str__(self):
        return self.name