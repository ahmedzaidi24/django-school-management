from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255)
    coordinator = models.CharField(max_length=255)
    size = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def total_students(self):
        return self.student_set.count()  # Count the number of students enrolled in this course

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    student_id = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


