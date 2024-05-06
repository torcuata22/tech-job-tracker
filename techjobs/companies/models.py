from django.db import models
from django.utils.timezone import now


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"
        
    name = models.CharField(max_length=50, unique=True, null=False)
    status = models.CharField(max_length=50 ,choices = CompanyStatus.choices, default=CompanyStatus.HIRING)
    lastt_update = models.DateTimeField(default = now, editable=True)
    notes = models.CharField(max_length=100, blank=True)
    