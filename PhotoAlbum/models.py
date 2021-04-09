from django.db import models

# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to ='images/')

    def __str__(self):
        return str(self.id)
    
class Classification(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to ='results/')
    label = models.CharField(max_length = 50,default='AEROPLANE')
    classification_category = models.CharField(max_length = 50,default='')
    probability = models.IntegerField()

    def __str__(self):
        return str(self.id)
    