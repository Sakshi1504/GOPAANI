from django.db import models

# Create your models here.
class GoPaani(models.Model):
    price=models.CharField(max_length=100)
    version=models.CharField(max_length=100)
    artistName=models.CharField(max_length=100)
    primaryGenreName=models.CharField(max_length=100)
    lookupkey=models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.artistName