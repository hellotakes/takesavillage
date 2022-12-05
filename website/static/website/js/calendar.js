document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    if (calendarEl !== null){
        var calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'timeGridWeek',
            themeSystem: 'bootstrap5',
            height: "auto",
            allDaySlot: false,
            slotMinTime: '6:00',
            slotMaxTime: '20:00',
        });
        calendar.render();
    }
});

