from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Teams(models.Model):

    class TeamChoices(models.TextChoices):
        T1 = 'Rajsthan Royals',_("Rajsthan Royals")
        T2 = 'Mumbai Indians',_("Mumbai Indians")
        T3 = 'Royal Challengers Bangalore',_("Royal Challengers Bangalore")
        T4 = "Chennai Super Kings",_("Chennai Super Kings")
        T5 = "Delhi Capitals",_("Delhi Capitals")
        T6 = "Sun Risers Hyderabad",_("Sun Risers Hyderabad")
        T7 = "Kolkata Knight Riders",_("Kolkata Knight Riders")
        T8 = "Punjab Kings",_("Punjab Kings")
        

    TeamId     = models.TextField(max_length=4,primary_key=True)
    TeamName   = models.TextField(max_length=100,choices=TeamChoices.choices)
    TeamIcon   = models.ImageField(upload_to='icons',blank=True)
    TopBatsman = models.TextField(max_length=100,blank=True)
    TopBowler  = models.TextField(max_length=100,blank=True)
    TourWon    = models.IntegerField(default=0)

    def __str__(self):
        return self.TeamName

class Players(models.Model):
    name = models.TextField(max_length=50,blank=False,null=False)
    team = models.ForeignKey(Teams,on_delete=models.DO_NOTHING)
    price = models.TextField(max_length=100,default=0)
    isPlaying = models.BooleanField(default=True)
    description= models.TextField(max_length=100,choices=(('BT',_("Batsman")),
    ('BO',_("Bowler")),
    ('AR',_("All Rounder"))))
    pic = models.ImageField(upload_to='players_pics',default='default-player.png')
    def __str__(self):
        return self.name
