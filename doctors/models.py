from django.db import models

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    crm = models.IntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name

