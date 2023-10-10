from django.db import models
from jsonfield import JSONField


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    display = models.CharField(max_length=255)
    fields = JSONField(null=True)
    keys = JSONField(null=True)

    def __str__(self):
        return self.name


class IPList(models.Model):
    ip = models.CharField(max_length=255, unique=True)
    product = models.ForeignKey(
        Product, related_name="ip_list", on_delete=models.PROTECT)

    def __str__(self):
        return "{} - ({})".format(self.ip, self.product)
