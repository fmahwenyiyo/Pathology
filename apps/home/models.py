# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
###########################################################################
class Contact(models.Model): 
   id = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=50) 
   city = models.CharField(max_length=50) 
   state = models.CharField(max_length=2) 
   create_date = models.DateTimeField() 
   phone_number = models.CharField(max_length=20) 
   email = models.CharField(max_length=20) 

   def __str__(self): 
      return self.name 

##########################################################################
class Customer(models.Model): 
   id = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=50) 
   city = models.CharField(max_length=50) 
   state = models.CharField(max_length=2) 
   create_date = models.DateTimeField() 
   phone_number = models.CharField(max_length=20) 
   email = models.CharField(max_length=20) 

   def __str__(self): 
      return self.name 
   
   
##########################################################################
class Symptom(models.Model):
   id = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=100)
   description = models.TextField()
   
   def __str__(self):
      return self.name

##########################################################################
class DiseaseClass (models.Model):
   id = models.IntegerField(primary_key=True)
   code = models.CharField(max_length=20)
   name = models.CharField(max_length=100)
   description = models.TextField()
   
   def __str__(self):
      return self.name
  
########################################################################## 
class Disease (models.Model):
   id = models.IntegerField(primary_key=True)
   disease_class = models.ForeignKey(DiseaseClass, on_delete=models.CASCADE)
   name = models.CharField(max_length=100)
   
   def __str__(self):
      return self.name
  
##########################################################################  
class Treatment(models.Model):
   id = models.IntegerField(primary_key=True)
   disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
   process_name = models.CharField(max_length=100)
   description = models.TextField()
   
   def __str__(self):
      return self.process_name
###########################################################################

class DiseaseSymptom(models.Model):
   id = models.UUIDField(
      primary_key = True,
      default = uuid.uuid4,
      editable = False
      )
   name = models.CharField(max_length=100)
   disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
   symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
   
   def __str__(self):
      return self.name
###########################################################################