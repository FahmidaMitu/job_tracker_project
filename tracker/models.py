from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Wishlist', 'Wishlist'),
        ('Applied', 'Applied'),
        ('Screening', 'Screening'),
        ('Interview', 'Interview'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_description = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=50, blank=True, null=True)
    job_url = models.URLField(blank=True, null=True)
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Wishlist')
    notes = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f"{self.job_title} - {self.company_name}"

class Interview(models.Model):
    INTERVIEW_TYPES = [
        ('Phone', 'Phone Screening'),
        ('Technical', 'Technical Interview'),
        ('Managerial', 'Managerial Interview'),
        ('HR', 'HR Interview'),
    ]

    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='interviews')
    interview_date = models.DateTimeField()
    interview_type = models.CharField(max_length=20, choices=INTERVIEW_TYPES)
    meeting_link = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_application.job_title} - {self.interview_type}"