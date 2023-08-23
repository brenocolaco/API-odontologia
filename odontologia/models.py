from django.db import models

# Create your models here.
class ACD(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=False, max_length=30,)
    telefone = models.CharField(max_length=14)
    dia_da_semana = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
