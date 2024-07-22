from django.db import models

# Create your models here.
class VehicleInventory(models.Model):
    make=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    year=models.IntegerField()
    price=models.FloatField()
    color=models.CharField(max_length=20)
    
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class TestDrive(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    vehicle=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name