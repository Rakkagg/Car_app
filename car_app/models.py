from django.db import models

class Car(models.Model):
    carName = models.CharField(max_length=50)
    carColor = models.CharField(max_length=50)
    carPosition = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.carName} - {self.carColor} - {self.carPosition}"




