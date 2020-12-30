from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return '<User: ' + str(self.id) + ',' + \
                self.name + ', ' + self.mail + ', ' + str(self.age) + '>'