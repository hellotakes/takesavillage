import datetime
import itertools
from typing import List, Dict, Iterable

import attrs


@attrs.define
class Slots:
    day: datetime.date
    duration: datetime.timedelta
    slots: List['datetime.time']

    def remove_slot(self, slot_to_remove: 'datetime.time') -> 'Slots':
        new_slots = [slot for slot in self.slots if slot != slot_to_remove]
        return attrs.evolve(self, slots=new_slots)

    def as_datetime(self) -> List['datetime.datetime']:
        return [datetime.datetime.combine(self.day, slot) for slot in self.slots]


class Booking:
    def __init__(self, from_day: 'datetime.date', appointments: List['datetime.datetime']):
        self.slots = self.get_slots_for_week(from_day)  # type: Dict['datetime.date', 'Slots']
        self.slots = self.filter_available_slots(self.slots, appointments)

    def as_list(self) -> Iterable[List['datetime.datetime']]:
        return itertools.zip_longest(
            *[slots.as_datetime() for slots in sorted(list(self.slots.values()), key=lambda s: s.day)],
            fillvalue=None
        )

    @classmethod
    def filter_available_slots(cls, slots: Dict['datetime.date', 'Slots'], appointments: List['datetime.datetime']) -> Dict['datetime.date', 'Slots']:
        result = slots.copy()
        for appointment in appointments:
            if appointment.date() not in slots:
                continue
            result[appointment.date()] = result[appointment.date()].remove_slot(appointment.time())
        return result

    @classmethod
    def get_slots_for_week(cls, from_day: 'datetime.date') -> Dict['datetime.date', 'Slots']:
        days = (from_day.replace(day=from_day.day + i) for i in range(0, 7))
        return {day: cls.get_slots(day) for day in days}

    @classmethod
    def get_slots(cls, for_day: datetime.date) -> 'Slots':
        first_slot = datetime.datetime.combine(for_day, datetime.time(hour=8))
        slot_duration = datetime.timedelta(minutes=30)

        return Slots(
            day=for_day,
            duration=slot_duration,
            slots=[(first_slot + (i * slot_duration)).time() for i in range(0, 20)]
        )


