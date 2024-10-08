# Generated by Django 5.1.1 on 2024-09-30 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_diagnosis_alter_patient_id_alter_patient_diagnosis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='diagnosis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patient_diagnois', to='patients.diagnosis'),
        ),
    ]
