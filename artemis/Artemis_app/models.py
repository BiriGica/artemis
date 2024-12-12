from django.db import models

# Create your models here.
class Usuário(models.Model):
    relato =  models.CharField (max_length=1500)


    #método da classe
    def registrar_relato (self):
        self.save()
