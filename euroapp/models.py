from django.db import models

class Chave(models.Model):
    numeros = models.CharField(max_length=100)
    estrelas = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numeros
