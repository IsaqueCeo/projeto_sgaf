from django.db import models

class Login(models.Model):
    matricula = models.IntegerField(max_length=100)
    senha = models.IntegerField(max_length=100)

    def __str__(self):
        return self.matricula
