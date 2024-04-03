from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.firstname + " " + self.lastname