from django.db import models

# Create your models here.
class PSD(models.Model):
    PSD_value = models.FloatField(blank=True, default=0)
    Freq_value = models.FloatField(blank=True, default=0)

    PSD_svg = models.FloatField(blank=True, default=0)
    Freq_svg = models.FloatField(blank=True, default=0)

    sc_tag = models.CharField(blank=True, max_length=200)
