from django.db import models

# Create your models here.
class Emp(models.Model):
    empid=models.CharField(max_length=50, required=False)
    ename=models.CharField(max_length=50, required=False)
    sal=models.CharField(max_length=50, required=False)
    deptno=models.CharField(max_length=50, required=False)
    username=models.CharField(max_length=50, required=False)
    pw=models.CharField(max_length=50, required=False)

    def __str__(self):
        return self.ename
    
class Student(models.Model):
    rollno=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    pno=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    cls=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class emp(models.Model):
    name=models.CharField(max_length=50)
    pno=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    pw=models.CharField(max_length=50)

    def __str__(self):
        return self.name

