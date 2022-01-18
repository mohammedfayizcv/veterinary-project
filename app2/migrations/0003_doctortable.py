# Generated by Django 3.2.9 on 2021-12-23 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_nursetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fristname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(max_length=10)),
                ('startdate', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.doctordepartment')),
            ],
        ),
    ]
