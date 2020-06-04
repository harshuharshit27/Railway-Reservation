from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Station(models.Model):
    ''' Station '''
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Route(models.Model):
    ''' Route '''
    name = models.CharField(max_length=20)
    source = models.ForeignKey('Station', related_name='source', on_delete=models.CASCADE)
    destination = models.ForeignKey('Station', related_name='destination', on_delete=models.CASCADE)
    route_path = models.ManyToManyField("Station", through="RoutePath")

    def __str__(self):
        return self.name
        
class RoutePath(models.Model):
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    station = models.ForeignKey('Station', on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return "%s-%s-%d" % (self.route.name, self.station.name, self.order)

class Train(models.Model):
    ''' Train Information '''
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=300)
    date = models.DateField()
    departure = models.TimeField(blank=True, null=True)
    arrival = models.TimeField(blank=True, null=True)
    route = models.ForeignKey('Route',on_delete=models.CASCADE)
    third_ac = models.IntegerField(default=10)
    second_ac = models.IntegerField(default=10)
    sleeper = models.IntegerField(default=10)

    def __str__(self):
        return self.name

    def decrease_third_ac(self):
        self.third_ac -= 1
        self.save()

    def decrease_second_ac(self):
        self.second_ac -= 1
        self.save()

    def decrease_sleeper(self):
        self.second_ac -= 1
        self.save()


class Ticket(models.Model):
    ''' Ticket '''
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    train = models.ForeignKey('Train', on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=0)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name + self.last_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
