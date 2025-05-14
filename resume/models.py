from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume_file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    skills = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)

    def __str__(self):
        return self.name