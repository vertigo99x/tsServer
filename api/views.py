from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response 


from .models import Match
# Create your views here.
from .serializers import MatchSerializer
from threading import Thread
import time
from django.conf import settings
def addEvent():
    try:
        while True:
            with open(rf"{settings.BASE_DIR}/dataset.txt", "r+") as h:
                r = h.readlines()
                for c in r:
                    x=c.split(',')
                    hg,ag,date,ref,w,ht,at = x[4],x[5],x[1],x[10],x[6],x[2],x[3]
                    
                    da = Match.objects.create(
                        homeTeam = ht,
                        awayTeam = at,
                        homeGoals = hg,
                        awayGoals = ag,
                        winner = w,
                        referee = ref,
                        date_played = date
                    )
                    da.save();
                    
                    time.sleep(60)
    except Exception:
        
        pass


class MatchView(APIView):
    def get(self, request, *args, **kwargs):
        match = Match.objects.order_by('-dateCreated').first()
        serializer = MatchSerializer(match)
        return Response(serializer.data)
    

        
class MatchAllView(APIView):
    def get(self, request, *args, **kwargs):
        match = Match.objects.order_by('-dateCreated').all()
        serializer = MatchSerializer(match, many=True)
        return Response(serializer.data)
    

Thread(target=addEvent).start()
