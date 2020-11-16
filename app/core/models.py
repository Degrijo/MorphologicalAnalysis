import pymorphy2
from django.db import models


morph = pymorphy2.MorphAnalyzer()


class Document(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:15] + '...'
