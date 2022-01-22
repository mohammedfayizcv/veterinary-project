# Generated by Django 3.2.9 on 2022-01-14 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0016_alter_doctor_time_table_time'),
        ('app1', '0014_remove_appoinmenttable_token_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoinmenttable',
            name='token_number',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app2.doctor_time_table'),
            preserve_default=False,
        ),
    ]