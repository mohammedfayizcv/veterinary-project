# Generated by Django 3.2.9 on 2021-12-26 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0005_doctortable_image'),
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinmenttable',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.doctortable'),
        ),
    ]
