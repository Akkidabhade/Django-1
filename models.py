from django.db import models

class TeamDetails(models.Model):
    playerName=models.CharField(max_length=30)
    playerSurname=models.CharField(max_length=30)
    playerAge=models.CharField(max_length=30)
    playerSpeciality=models.CharField(max_length=30)
    playerHs=models.CharField(max_length=5)



