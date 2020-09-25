from django.db import models

# Create your models here.


class EmployeeInfo(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.EmailField()
	department = models.CharField(max_length = 50)
	date_of_birth = models.DateField()

	def __str__(self):
		return self.first_name
