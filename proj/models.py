from django.db import models

class Employee(models.Model):
    empid = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Locations(models.Model):
    # empid = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, related_name="Location", default='', blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Locations', null=True)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.city
    
