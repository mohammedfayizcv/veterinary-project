# Generated by Django 3.2.9 on 2022-01-14 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_appoinmenttable_token_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoinmenttable',
            name='token_number',
        ),
    ]