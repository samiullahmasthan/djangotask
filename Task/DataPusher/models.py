
from django.db import models
from django.utils.crypto import get_random_string
# Create your models here.


class Account(models.Model):
  
  email_id=models.EmailField(unique=True)
  account_id=models.CharField(unique=True,max_length=100)
  account_name=models.CharField(max_length=100)
  app_secret_token=models.CharField(max_length=100)
  website=models.URLField(blank=True)
  
  def save(self,*args,**kwargs):
    
    if not self.pk:
      self.app_secret_token=get_random_string(length=32)
      
      
    super().save(*args,**kwargs)
    
  def __str__(self):
    return self.account_name 
  
  
class Destination(models.Model):
  account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="destination")
  url=models.URLField()
  http_method=models.CharField(max_length=10)
  header=models.JSONField()
  
  
      
      
