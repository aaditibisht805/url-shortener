from django.db import models
from hashlib import md5
from django.core.validators import URLValidator 
from django.core.exceptions import ValidationError 
# Create your models here.
class Url(models.Model):
    full_url= models.URLField()
    short_url=models.CharField(unique=True, max_length=20)
    
    def __str__(self):
        return self.full_url
     
    @classmethod 
    def create(self, full_url):
        validator = URLValidator()
        try:
            validator(full_url)
        except ValidationError:
            return None 
        temp_url = md5(full_url.encode()).hexdigest()[:5]   #short url 
        
        try :
            obj= self.objects.create(full_url=full_url,short_url= temp_url ) #default create function call  
        except :
            obj= self.objects.get(full_url=full_url )
        obj.save()
        return obj
