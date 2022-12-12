from django.db import models
from django.utils.translation import gettext_lazy as _


class Sex(models.TextChoices):
    MALE = 'M', _('Male')
    FEMALE = 'F', _('Female')
    OTHER = 'O', _('Other')


class Language(models.TextChoices):
    FRENCH = 'FR', _('French')
    ENGLISH = 'EN', _('English')
    DUTCH = 'NL', _('Dutch')


class Speciality(models.TextChoices):
    # SPECIALITY = 'Lactation specialist', _('Lactation specialist'),
    LACTATION = 'Certified Breastfeeding Specialist', _('Certified Breastfeeding Specialist'),
    HYPNO_BIRTHING = 'HypnoBirthing® Childbirth Educator', _('HypnoBirthing® Childbirth Educator')

