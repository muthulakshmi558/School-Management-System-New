from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Student, Teacher, Course, Attendance, Marks

# Dashboard
def dashboard(request):
    return render(request, 'dashboard.html')

# Students page
def students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

# Teachers page
def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

# Courses page
def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

# Attendance page
def attendance(request):
    attendance = Attendance.objects.all()
    return render(request, 'attendance.html', {'attendance': attendance})

# Marks page
def marks(request):
    marks = Marks.objects.all()
    return render(request, 'marks.html', {'marks': marks})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Student, Attendance, Marks

def parent_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            student = Student.objects.get(parent_email=email)
            user = student.user  # get linked User

            if user.check_password(password):
                login(request, user)
                return redirect('parent_dashboard')
            else:
                error = "Invalid password"
        except Student.DoesNotExist:
            error = "Parent email not found"

        return render(request, 'parent_login.html', {'error': error})

    return render(request, 'parent_login.html')

def parent_dashboard(request):
    student = Student.objects.get(user=request.user)
    attendance = Attendance.objects.filter(student=student)
    marks = Marks.objects.filter(student=student)
    return render(request, 'parent_dashboard.html', {
        'student': student,
        'attendance': attendance,
        'marks': marks
    })