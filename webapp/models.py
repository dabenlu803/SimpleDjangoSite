from django.db import models


class PersonalInfo(models.Model):
    InfoId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    PhoneNum = models.CharField(max_length=30, null=False)
    Email = models.CharField(max_length=100, null=False)
    Location = models.CharField(max_length=100)
    Job = models.CharField(max_length=50)
    company = models.CharField(max_length=50)