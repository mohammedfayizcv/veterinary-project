# Generated by Django 3.2.9 on 2021-12-22 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctordepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofdepartment', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='staffCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StaffTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('phonenumber', models.BigIntegerField()),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=10)),
                ('startedDate', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=30)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.doctordepartment')),
                ('staffcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.staffcategory')),
            ],
        ),
    ]