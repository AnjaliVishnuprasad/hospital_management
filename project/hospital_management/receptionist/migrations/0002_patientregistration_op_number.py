# Generated by Django 5.0.3 on 2024-04-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientregistration',
            name='op_number',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]