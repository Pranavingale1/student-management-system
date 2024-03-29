from django.db import models

# Create your models here.

class student(models.Model):
    student_number = models.PositiveBigIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    CGPA = models.FloatField()

    def __str__(self) -> str:
        return f'Student - {self.first_name} {self.last_name}'