# Generated by Django 3.0.2 on 2020-02-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0012_company_topremark'),
    ]

    operations = [
        migrations.AddField(
            model_name='remarks',
            name='POC',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
