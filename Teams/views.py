from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Teams,Players

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PlayersSerializer
# Create your views here.
def home(request):

    teams = Teams.objects.all()
    
    return render(request,'allteam.html',{"teams":teams})

def TeamProfile(request,pk):

    team = Teams.objects.get(TeamId=pk)
    players = Players.objects.filter(team=team)

    return render(request,'teamprofile.html',{'players':players,'team':team})

@api_view(["GET"])
def AllPlayersAPI(request):
    players = Players.objects.all()
    serializer = PlayersSerializer(players,many=True) 
    return Response(serializer.data)