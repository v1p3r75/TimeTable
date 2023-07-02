from django.urls import path
from . import views

urlpatterns = [
    path("admin", views.adminDashboard, name="admin-dashboard"),
    path("", views.studentDashboard, name="student-dashboard"),
    path("dash", views.studentDash, name="student-dash"),
    path("admin/dash", views.adminDash, name="admin-dash"),
    path("admin/teachers", views.adminTeachers, name="admin-teachers"),
    path("admin/subjects", views.adminSubjects, name="admin-subjects"),
    path("admin/levels", views.adminLevels, name="admin-levels"),
    path("admin/classrooms", views.adminClassrooms, name="admin-classrooms"),
    path("admin/timetables", views.adminTimetables, name="admin-timetables"),
    path("admin/colaborators", views.adminColaborators, name="admin-colaborators"),
    path("weeks/<int:level>/<int:week>", views.adminViewTimetable, name="admin-weeks"),
    path("account", views.userAccount, name="user-account"),
    path("timetables", views.userTimetable, name="user-timetables"),
    path("teachers/timetables", views.teacherTimetable, name="teacher-timetables"),
    path("teachers/weeks/<int:week>", views.teacherWeek, name="teacher-weeks"),
    path("weeks/<int:week>", views.timeTableWeek, name="timetables-week"),
    path("faq", views.faq, name="user-faq"),
]