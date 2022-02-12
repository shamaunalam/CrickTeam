from django.http import HttpResponse
from django.shortcuts import render
from .models import Teams,Players


# Create your views here.
def home(request):

    teams = Teams.objects.all()
    
    return render(request,'allteam.html',{"teams":teams})

def TeamProfile(request,pk):

    team = Teams.objects.get(TeamId=pk)
    players = Players.objects.filter(team=team)

    return render(request,'teamprofile.html',{'players':players})
