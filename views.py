from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse



from django.shortcuts import render
from .models import Course,Student

def courses(request):
    coursesQuerySet = Course.objects.all()
    return render(request, 'courses.html' , { 'courses' : coursesQuerySet})


def students(request):
    studentsQuerySet = Student.objects.all()
    return render(request, 'Students.html' , { 'students' : studentsQuerySet})


def singlecourse(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = course.student_set.all()
    total_students = course.total_students()
    return render(request, 'singlecourse.html', {'course': course, 'students': students, 'total_students': total_students})