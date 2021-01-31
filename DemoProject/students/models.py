from django.db import models


class StudentModel(models.Model):
    Name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.Name