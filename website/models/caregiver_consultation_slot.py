from django.db import models

from website.models.choices import WeekDays


class CaregiverConsultationSlot(models.Model):
    specialist = models.ForeignKey("website.Caregiver", on_delete=models.PROTECT, related_name="consultation_slots")

    week_day = models.CharField(max_length=60, choices=WeekDays.choices)
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return f"{self.specialist}  {self.week_day}: {self.start} -> {self.end}"

    def numeric_iso_week_day(self) -> int:
        return {
            WeekDays.MONDAY.name: 1,
            WeekDays.TUESDAY.name: 2,
            WeekDays.WEDNESDAY.name: 3,
            WeekDays.THURSDAY.name: 5,
            WeekDays.FRIDAY.name: 5,
            WeekDays.SATURDAY.name: 6,
            WeekDays.SUNDAY.name: 7,
        }[self.week_day]
