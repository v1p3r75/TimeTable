from django.db.models import Q, Sum, F
from datetime import datetime, timedelta
from django.utils import timezone
from .models import TimeTable
import calendar
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import threading
import string
import random

def get_timetable_by_level():

    timetable_entries = TimeTable.objects.select_related('level', 'user', 'classroom', 'subject')

    # Créez un dictionnaire pour stocker les données groupées par filière, semaine et jour
    grouped_timetable = {}
    level_id = None

    # Parcourez les emplois du temps et groupez les données
    for entry in timetable_entries:
        level_label = entry.level.label
        week_number = entry.start_time.isocalendar()[1]
        day_name = entry.start_time.strftime('%A')

        if level_label not in grouped_timetable:
            grouped_timetable[level_label] = {}

        if week_number not in grouped_timetable[level_label]:
            grouped_timetable[level_label][week_number] = []

        day_data = {
            'id': entry.id,
            'user_id': entry.user.id,
            'user': str(entry.user),
            'level_id': entry.level.id,
            'level': entry.level.label,
            'classroom_id': entry.classroom.id,
            'classroom': entry.classroom.label,
            'subject_id': entry.subject.id,
            'subject': entry.subject.label,
            'start_time': str(entry.start_time),
            'end_time': str(entry.end_time),
        }
        level_id = entry.level.id

        grouped_timetable[level_label][week_number].append({day_name: day_data})

    # Affichez les données groupées par filière, semaine et jour
    result = []

    for level_label, level_data in grouped_timetable.items():
        level_info = {'level': level_label,'level_id' : level_id, 'weeks': []}
        
        for week_number, week_data in level_data.items():
            week_info = {'week': week_number, 'days': []}

            for day_data in week_data:
                day_name, day_info = list(day_data.items())[0]
                day_info['day_name'] = day_name.capitalize()
                week_info['days'].append(day_info)

            level_info['weeks'].append(week_info)

        result.append(level_info)

    return result

def get_timetable_global():


    timetable_entries = TimeTable.objects.select_related('level', 'user', 'classroom', 'subject')

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
            'subject': entry.subject.label,
            'start_time': str(entry.start_time),
            'end_time': str(entry.end_time),
        }}
        grouped_timetable[week_number].append(day_data)

    # Affichez les données groupées par semaine et jour
    result = []

    for week_number, week_data in grouped_timetable.items():
        week_info = {'week': week_number, 'days': []}
        
        for day_data in week_data:
            day_name, day_info = list(day_data.items())[0]
            day_info['day_name'] = day_name.capitalize()
            week_info['days'].append(day_info)

        result.append(week_info)

    return result

def get_data(timetable_entries):
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
            'classroom_desc': entry.classroom.description,
            'subject': entry.subject.label,
            'start_time': str(entry.start_time),
            'end_time': str(entry.end_time),
        }}
        grouped_timetable[week_number].append(day_data)

    # Affichez les données groupées par semaine et jour
    result = []

    for week_number, week_data in grouped_timetable.items():
        week_info = {'week': week_number, 'days': []}
        
        for day_data in week_data:
            day_name, day_info = list(day_data.items())[0]
            day_info['day_name'] = day_name.capitalize()
            week_info['days'].append(day_info)

        result.append(week_info)

    return result

def get_timetable_data(level_id : int | None = None, current_week : bool = False, week = None):

    # Récupérez les emplois du temps avec les informations associées pour toutes les semaines
    if current_week:

        start_date = datetime.now().date() - timedelta(days = datetime.now().date().weekday() - 0)
        end_date = start_date + timedelta(days = 6)
        timetable_entries = TimeTable.objects\
            .filter(Q(start_time__date__gte = start_date, end_time__date__lte = end_date), level_id = level_id)\
            .select_related('level', 'user', 'classroom', 'subject')
    else:
        timetable_entries = TimeTable.objects.filter(level_id = level_id, week = week).select_related('level', 'user', 'classroom', 'subject')

    result = get_data(timetable_entries)

    return result

def get_timetable_user(user_id : int | None = None, current_week : bool = False, week = None):

    # Récupérez les emplois du temps avec les informations associées pour toutes les semaines
    if current_week:

        start_date = datetime.now().date() - timedelta(days = datetime.now().date().weekday() - 0)
        end_date = start_date + timedelta(days = 6)
        timetable_entries = TimeTable.objects\
            .filter(Q(start_time__date__gte = start_date, end_time__date__lte = end_date), user_id = user_id)\
            .select_related('level', 'user', 'classroom', 'subject')
    else:
        timetable_entries = TimeTable.objects.filter(user_id = user_id, week = week).select_related('level', 'user', 'classroom', 'subject')

    result = get_data(timetable_entries)

    return result

def get_student_stat(type, level_id):

    current_date = timezone.now().date()

    current_week = current_date.isocalendar()[1]

    if type == 'week_total_hourse':

        total_hours = TimeTable.objects.filter(
            week=current_week, level_id=level_id
        ).aggregate(total_hours=Sum(F('end_time') - F('start_time'))).get('total_hours')


        return int(total_hours.total_seconds() // 3600) if total_hours is not None else 0
    

    if type == 'total_subjects':


        total = TimeTable.objects.filter(
            week=current_week, level_id=level_id
        ).count()

        return total
    
    if type == 'week_days':

        most_busy_day = TimeTable.objects.filter(
            week=current_week, level_id=level_id
        ).values('start_time__week_day').annotate(
            total_hours=Sum(F('end_time') - F('start_time'))
        ).order_by('-total_hours').first()

        # Effectuer l'agrégation pour trouver le jour le moins chargé
        least_busy_day = TimeTable.objects.filter(
            week=current_week, level_id=level_id
        ).values('start_time__week_day').annotate(
            total_hours=Sum(F('end_time') - F('start_time'))
        ).order_by('total_hours').first()

        # Extraire les numéros de jour de la semaine (1 pour lundi, 2 pour mardi, etc.)
        most_busy_day_number = most_busy_day['start_time__week_day'] if most_busy_day is not None else None
        least_busy_day_number = least_busy_day['start_time__week_day'] if most_busy_day is not None else None

        most = calendar.day_name[most_busy_day_number-1] if most_busy_day_number is not None else "Aucun"
        least = calendar.day_name[least_busy_day_number-1] if least_busy_day_number is not None else "Aucun"

        return most, least

def get_teacher_info(type, user_id):

    current_date = timezone.now().date()

    current_week = current_date.isocalendar()[1]

    if type == 'week_total_hourse':

        total_hours = TimeTable.objects.filter(
            week=current_week, user_id=user_id
        ).aggregate(total_hours=Sum(F('end_time') - F('start_time'))).get('total_hours')


        return int(total_hours.total_seconds() // 3600) if total_hours is not None else 0
    
    if type == 'total_subjects':


        total = TimeTable.objects.filter(
            week=current_week, user_id=user_id
        ).count()

        return total
    
    if type == 'week_days':

        most_busy_day = TimeTable.objects.filter(
            week=current_week, user_id=user_id
        ).values('start_time__week_day').annotate(
            total_hours=Sum(F('end_time') - F('start_time'))
        ).order_by('-total_hours').first()

        # Effectuer l'agrégation pour trouver le jour le moins chargé
        least_busy_day = TimeTable.objects.filter(
            week=current_week, user_id=user_id
        ).values('start_time__week_day').annotate(
            total_hours=Sum(F('end_time') - F('start_time'))
        ).order_by('total_hours').first()

        # Extraire les numéros de jour de la semaine (1 pour lundi, 2 pour mardi, etc.)
        most_busy_day_number = most_busy_day['start_time__week_day'] if most_busy_day is not None else None
        least_busy_day_number = least_busy_day['start_time__week_day'] if most_busy_day is not None else None

        most = calendar.day_name[most_busy_day_number-1] if most_busy_day_number is not None else "Aucun"
        least = calendar.day_name[least_busy_day_number-1] if least_busy_day_number is not None else "Aucun"

        return most, least
    

def send_notification(subject, recipient_list, template, context = {}):

    html = render_to_string(template, context)

    html_tags = strip_tags(html)

    try:

        email = EmailMultiAlternatives(
            subject,
            html,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,

        )
        email.attach_alternative(html, "text/html")
        thread = threading.Thread(target=email.send)
        thread.deamon = True
        thread.start()


    except Exception as e:
        print('Failed to send notification : ', e)

def generate_password(length = 8):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def get_total_hours(subject_id):

    total_hours = TimeTable.objects.filter(subject_id=subject_id)\
    .aggregate(total=Sum('end_time' - 'start_time'))['total']
    
    return total_hours