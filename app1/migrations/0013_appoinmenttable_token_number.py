# Generated by Django 3.2.9 on 2022-01-14 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0016_alter_doctor_time_table_time'),
        ('app1', '0012_remove_appoinmenttable_token_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoinmenttable',
            name='token_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app2.doctor_time_table'),
        ),
    ]
