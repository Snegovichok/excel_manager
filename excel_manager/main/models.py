from django.db import models
from django.contrib.auth.models import User

class ExcelFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='excel_files/', max_length=1024)
    allowed_organizations = models.ManyToManyField(User, blank=True, related_name='excel_files')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
