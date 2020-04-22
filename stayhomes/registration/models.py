from django.db import models


# Create your models here.
class loginform(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    DateOfBirth = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    Email = models.CharField(max_length=25)
    Phone = models.CharField(max_length=10)
    Education = models.CharField(max_length=25)

    def _str_(self):
        return self.Name

    class Meta:
        db_table = 'loginform'
