from django.http import HttpResponse
from django.shortcuts import render
from .models import Teams,Players


# Create your views here.
def home(request):
    
    team = Teams.objects.all()

    return render(request,'team.html',{'teams':team})


def TeamPage(request,pk):

    team = Teams.objects.get(TeamId=pk)
    players = Players.objects.filter(team=team)

    return render(request,'team.html')



    