# Generated by Django 3.2.9 on 2022-01-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0013_doctor_time_table_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_time_table',
            name='end_time',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_time_table',
            name='time',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
