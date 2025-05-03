from django.db import models

class Ward(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    capacity = models.IntegerField()

class Team(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
