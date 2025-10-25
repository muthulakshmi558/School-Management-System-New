from django.contrib import admin
from .models import Course, Teacher, Student, Attendance, Marks

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'parent_email')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'date', 'status')

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'subject', 'marks_obtained')
