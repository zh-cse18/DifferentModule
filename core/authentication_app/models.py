from django.db import models

# Registration model
class Register(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)
