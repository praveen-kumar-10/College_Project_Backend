from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
	email = models.TextField(default=None, null=True, unique=True)
	password = models.TextField(default=None, null=True)
	user_type = models.TextField(default=None, null=True) # student, teacher, local_admin, super_admin
	verified = models.BooleanField(default=False, null=True)
	is_active = models.BooleanField(default=False, null=True)

	def __str__(self):
		return self.email


class Teacher(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.TextField(default=None,null=False)
	gender = models.TextField(default=None,null=True)
	phone = models.CharField(default=None,null=False,max_length=10,unique=True)
	department = models.TextField(default=None,null=False)

	def __str__(self) :
		return self.name

# class Student(models.Model):
# 	user = models.ForeignKey(User)
# 	student_data = "19BQ..."
# 	# class_obj = models.ForeignKey(Class)


# class Class(models.Model):
# 	year = models.TextField() # 2019 etc
# 	edu_year = models.TextField() # 1st, 2nd etc
# 	branch = models.TextField()
# 	section = models.TextField()
# 	semister = models.TextField()


# class Lectures(models.Model):
# 	class_obj = models.ForeignKey(Class)
# 	teacher = models.ForeignKey(Teacher)
# 	subject = models.TextField()


# class StudentClassMapping(models.Model):
# 	class_obj = models.ForeignKey(Class)
# 	student = models.ForeignKey(Student)


# class Assignment(models.Model):
# 	title = models.TextField()
# 	due_date = models.DateTimeField()
# 	assignment_link = models.TextField()


# class AssignmentAssigned(models.Model):
# 	assignment = models.ForeignKey(Assignment)
# 	student = models.ForeignKey(Student)

