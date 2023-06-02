from djongo import models

class TestData(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Add more fields as per your requirements
