from django.db import models


class MobileInfo(models.Model):
    IMEI1 = models.CharField(max_length=100)
    IMEI2 = models.CharField(max_length=100)
    MAC_ID = models.CharField(max_length=100)
    Status = models.IntegerField()
    Competitor = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.IMEI1

    def __str__(self):
        return self.IMEI2

    def __str__(self):
        return self.MAC_ID

    def __str__(self):
        return self.Status

    def __str__(self):
        return self.Competitor
