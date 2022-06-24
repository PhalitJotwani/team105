from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=10,null=False)
    def __str__(self) :
        return self.name

class Volunteer(models.Model):
    vol_id = models.IntegerField(null=False,primary_key=True)
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender,null=True,on_delete=models.SET_NULL)
    age = models.IntegerField(null=False)
    email = models.CharField(max_length=100,null=False)
    phone = models.IntegerField(null=False)
    def __str__(self):
        return '%d %s %s %d'%(self.vol_id,self.first_name, self.last_name,self.phone)
    
class End_user(models.Model):
    user_id = models.IntegerField(null=False,primary_key=True)
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender,null=True,on_delete=models.SET_NULL)
    age = models.IntegerField(null=False)
    occupation = models.CharField(max_length=100)
    phone = models.IntegerField(null=False)
    registered_by  = models.ForeignKey(Volunteer,on_delete=models.CASCADE)
    
    def __str__(self):
        return '%d %s %s %d'%(self.user_id,self.first_name, self.last_name,self.phone)
    
class Family_grp(models.Model):
    family_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(End_user,on_delete=models.CASCADE)
    def __str__(self):
        return '%d %d'%(self.family_id,self.user_id)
 
 
class Scheme(models.Model):
    scheme_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    desc = models.TextField(max_length=500)
    def __str__(self):
        return self.name    
class Linked_Scheme(models.Model):
    user_id = models.ForeignKey(End_user,on_delete=models.CASCADE)
    scheme_id = models.ForeignKey(Scheme,on_delete=models.CASCADE)
    vol_id = models.ForeignKey(Volunteer,null=True,on_delete=models.SET_NULL)
    date_joined = models.DateTimeField()
    def __str__(self):
        return '%s'%(self.date_joined.strftime("%d/%m/%Y , %H;%M;%S"))  

