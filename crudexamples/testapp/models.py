from django.db import models
class Employe(models.Model):
    id=models.IntegerField
    name=models.CharField(max_length=30)
    sal=models.FloatField()

    class Meta:
        db_table='emp'
# Create your models here.
