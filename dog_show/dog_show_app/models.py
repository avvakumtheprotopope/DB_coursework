from django.db import models
from django.db.models import PositiveSmallIntegerField, IntegerField, ForeignKey, PositiveIntegerField, OneToOneField


class Owner(models.Model):
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    club = ForeignKey('Club', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



class Breed(models.Model):
    name = models.CharField(unique=True, max_length=50)
    ring = OneToOneField('Ring', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ring(models.Model):
    number = PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return str(self.number)

class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = PositiveSmallIntegerField()
    breed = ForeignKey(Breed, on_delete=models.CASCADE, related_name='dogs')
    mom = models.CharField(max_length=50)
    dad = models.CharField(max_length=50)
    owner = ForeignKey('Owner', on_delete=models.CASCADE, related_name='dogs')
    club = ForeignKey('Club', on_delete=models.CASCADE, related_name='dogs')
    number = PositiveIntegerField(unique=True)
    grade = PositiveIntegerField()

    def __str__(self):
        return str(self.number)

class Club(models.Model):
    name = models.CharField(unique=True, max_length=50)
    lower = IntegerField(unique=True)
    upper = IntegerField(unique=True)

    def __str__(self):
        return self.name



class Expert(models.Model):
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    breed = ForeignKey('Breed', on_delete=models.CASCADE, null=True, blank=True, related_name='experts')
    club = ForeignKey('Club', on_delete=models.CASCADE, related_name='experts')

    def __str__(self):
        return str(self.id)

