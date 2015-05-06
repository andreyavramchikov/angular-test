from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=255, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    cost = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    image_url = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return str(self.name)



