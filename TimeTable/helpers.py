from django.db.models import Min, Max
from datetime import timedelta
from .models import TimeTable

def get_timetable_data():

    # Obtention de la date de début et de fin de chaque semaine
    start_week = TimeTable.objects.aggregate(start=Min('start_time'))['start']
    end_week = TimeTable.objects.aggregate(end=Max('end_time'))['end']

    # Ajustement des dates de début et de fin pour correspondre à la semaine
    start_week = start_week - timedelta(days=start_week.weekday())
    end_week = end_week + timedelta(days=6 - end_week.weekday())

    # Regroupement des emplois du temps par semaine
    weekly_timetable = TimeTable.objects \
        .filter(start_time__gte=start_week, end_time__lte=end_week) \
        .values('week') \
        .annotate(start=Min('start_time'), end=Max('end_time'))
    

    return weekly_timetable