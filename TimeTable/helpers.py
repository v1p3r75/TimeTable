from django.db.models import Min, Max
from datetime import timedelta
from .models import TimeTable

def get_timetable_data(level_id = None):

        # Récupérez les emplois du temps avec les informations associées pour toutes les semaines
    timetable_entries = TimeTable.objects.filter(level_id = level_id).select_related('level', 'user', 'classroom', 'subject')

    # Créez un dictionnaire pour stocker les données groupées par semaine et jour
    grouped_timetable = {}

    # Parcourez les emplois du temps et groupez les données
    for entry in timetable_entries:
        week_number = entry.start_time.isocalendar()[1]
        day_name = entry.start_time.strftime('%A')

        if week_number not in grouped_timetable:
            grouped_timetable[week_number] = []

        day_data = {day_name: {
            'user': entry.user,
            'level': entry.level.label,
            'classroom': entry.classroom.label,
            'subjects': entry.subject.label
        }}
        grouped_timetable[week_number].append(day_data)

    # Affichez les données groupées par semaine et jour
    result = []

    for week_number, week_data in grouped_timetable.items():
        week_info = {'week': week_number, 'days': []}
        
        for day_data in week_data:
            day_name, day_info = list(day_data.items())[0]
            day_info['day_name'] = day_name
            week_info['days'].append(day_info)

        result.append(week_info)

    return result