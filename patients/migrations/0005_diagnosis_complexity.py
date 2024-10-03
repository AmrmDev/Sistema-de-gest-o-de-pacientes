# Generated by Django 5.1.1 on 2024-10-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_patient_diagnosis'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='complexity',
            field=models.CharField(choices=[('B', 'Baixa'), ('M', 'Média'), ('A', 'Alta'), ('E', 'Extrema')], default='M', max_length=10),
        ),
    ]
