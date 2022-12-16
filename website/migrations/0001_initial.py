# Generated by Django 4.1.4 on 2022-12-16 18:27

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Caregiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=240)),
                ('last_name', models.CharField(max_length=240)),
                ('email', models.EmailField(max_length=240)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('profile_photo', models.ImageField(upload_to='caregivers/profile/')),
                ('profile_video', models.URLField()),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('FR', 'French'), ('EN', 'English'), ('NL', 'Dutch'), ('PT', 'Portuguese')], max_length=2), size=3)),
                ('description', models.TextField(max_length=640)),
                ('physical', models.BooleanField(default=True)),
                ('online', models.BooleanField(default=False)),
                ('conditions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), size=5)),
                ('ranking', models.FloatField()),
                ('number_comments', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CaregiverAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=128)),
                ('street_no', models.CharField(max_length=4)),
                ('postal_code', models.IntegerField()),
                ('city', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=64)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CaregiverSpeciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(choices=[(None, ''), ('Certified Breastfeeding Specialist', 'Certified Breastfeeding Specialist'), ('HypnoBirthing® Childbirth Educator', 'HypnoBirthing® Childbirth Educator'), ('Midwife', 'Midwife'), ('Doula', 'Doula'), ('Lactation/breastfeeding consultant', 'Lactation/breastfeeding consultant'), ('Babywearing specialist', 'Babywearing specialist'), ('Sleep specialist', 'Sleep specialist'), ('Pediatrician', 'Pediatrician'), ('Perinatal psychologist', 'Perinatal psychologist'), ('Physical therapist', 'Physical therapist'), ('Periadtrician', 'Periadtrician'), ('Pre/post natal yoga teacher', 'Pre/post natal yoga teacher'), ('Pre/post natal massage', 'Pre/post natal massage'), ('Baby massage', 'Baby massage'), ('Pre/post natal physical therapist', 'Pre/post natal physical therapist'), ('Osteopath', 'Osteopath'), ('Parenting coach', 'Parenting coach'), ('Psychomotrician', 'Psychomotrician')], max_length=240)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('caregiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.caregiver')),
            ],
        ),
        migrations.CreateModel(
            name='CaregiverDiploma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('year', models.PositiveIntegerField()),
                ('caregiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.caregiver')),
            ],
        ),
        migrations.CreateModel(
            name='CaregiverConsultationSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=60)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.parent')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.caregiver')),
            ],
        ),
        migrations.AddField(
            model_name='caregiver',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='website.caregiveraddress'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('booked_on', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.parent')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.caregiver')),
            ],
        ),
    ]
