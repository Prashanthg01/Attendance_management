# attendance/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Attendance


def home(request):
    academic_year = request.GET.get('academic_year')
    semester = request.GET.get('semester')
    section = request.GET.get('section')
    students = Student.objects.filter(academic_year=academic_year, semester=semester, section=section)
    attendance_records = []
    class_name = ''
    session = ''
    datee = ''

    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        session = request.POST.get('session')
        datee = request.POST.get('datee')
        for student in students:
            is_present = request.POST.get(f'student-{student.id}', False)
            Attendance.objects.create(student=student, status=is_present, class_name=class_name, session=session, datee=datee)
        messages.success(request, 'Attendance has been submitted successfully!')
        return redirect('home')

    if class_name:
        attendance_records = Attendance.objects.filter(class_name=class_name)
    
    if session:
        attendance_records = Attendance.objects.filter(session=session)
    
    if datee:
        attendance_records = Attendance.objects.filter(datee=datee)

    return render(request, 'attendance/home.html', {
        'students': students,
        'attendance_records': attendance_records,
        'class_name': class_name,
        'datee': datee,
        'session': session,
    })

def result(request):
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        session = request.POST.get('session')
        datee = request.POST.get('datee')
        attendances = Attendance.objects.filter(class_name=class_name, session=session, datee=datee)
        return render(request, 'attendance/result.html', {'attendances': attendances, 'session': session, 'datee': datee})
    return render(request, 'attendance/result.html')

    