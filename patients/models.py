from django.db import models

class Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    diagnosis = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.diagnosis


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    admission_date = models.DateField()
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.PROTECT, related_name='patient_diagnois')

    def __str__(self):
        return self.name
    
