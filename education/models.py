from django.db import models
import uuid

# Create your models here.

class Student(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    ACADEMIC_LEVEL_CHOICES = (
        ('P.1', 'Primary 1'),
        ('P.2', 'Primary 2'),
        ('P.3', 'Primary 3'),
        ('P.4', 'Primary 4'),
        ('P.5', 'Primary 5'),
    )

    ENROLLMENT_STATUS_CHOICES = (
        ('actiive', 'Active'),
        ('dismissed', 'Dismissed'),
        ('graduated', 'Graduated'),
        ('transfered', 'Transferred'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    f_name = models.CharField('First Name', max_length=60)
    l_name = models.CharField('Last Name', max_length=60)
    dob = models.DateField('Birth Date')
    gender = models.CharField('gender', max_length=10, choices=GENDER_CHOICES, default='M')
    academic_level = models.CharField('Current Academic Level', max_length=10, choices=ACADEMIC_LEVEL_CHOICES)
    enrollment_status = models.CharField('Enrollment_status', max_length=20, choices=ENROLLMENT_STATUS_CHOICES)
    # photo = models.ImageField('Photo', upload_to='students/photos', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"