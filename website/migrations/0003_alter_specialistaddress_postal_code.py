# Generated by Django 4.1.3 on 2022-12-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_businesshours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialistaddress',
            name='postal_code',
            field=models.IntegerField(),
        ),
    ]
