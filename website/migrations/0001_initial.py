# Generated by Django 4.1.3 on 2022-11-29 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('physical', models.BooleanField(default=True)),
                ('online', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=640)),
                ('language', models.CharField(choices=[('FR', 'French'), ('EN', 'English'), ('NL', 'Dutch')], max_length=2)),
                ('speciality', models.CharField(choices=[], max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialistAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=128)),
                ('street_no', models.PositiveSmallIntegerField()),
                ('city', models.CharField(max_length=128)),
                ('postal_code', models.PositiveSmallIntegerField()),
                ('country', models.CharField(max_length=128)),
                ('specialist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', related_query_name='address', to='website.specialist')),
            ],
        ),
    ]
