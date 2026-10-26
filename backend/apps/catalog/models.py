from django.db import models



class Catalog(models.Model):
    title = models.CharField(max_length=155)