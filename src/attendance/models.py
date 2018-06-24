from django.db import models

# Create your models here.



class Student(models.Model):

	stu_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=20 , unique=True)
	sem = models.CharField(max_length=20)
	branch = models.CharField(max_length=20)


	def __str__(self):
		return self.name




class Calander(models.Model):
	student = models.OneToOneField(Student , on_delete=models.CASCADE )
	date = models.DateField(auto_now_add=True)
	status = models.CharField(max_length=5 , default='A')


	def __str__(self):
		return str(self.date)
