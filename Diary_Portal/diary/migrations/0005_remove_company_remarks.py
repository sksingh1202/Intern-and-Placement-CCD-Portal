# Generated by Django 3.0.2 on 2020-02-02 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_remarks_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='Remarks',
        ),
    ]
