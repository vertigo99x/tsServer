from django.db import models
from django.utils import timezone
# Create your models here.


class Match(models.Model):
    dateCreated = models.DateTimeField(default=timezone.now)
    homeTeam = models.CharField(max_length=25)
    awayTeam = models.CharField(max_length=25)
    homeGoals = models.IntegerField()
    awayGoals = models.IntegerField()
    winner = models.CharField(max_length=5)
    date_played = models.CharField(max_length=25)
    referee = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.homeTeam} vs {self.awayTeam}"

    def __unicode__(self):
        return f"{self.homeTeam} vs {self.awayTeam}"

    def matchData(self):
        if self.winner == "H":
            winner = self.homeTeam
        elif self.winner == "A":
            winner = self.awayTeam
        else:
            winner = None
        return {
            "match":f"{self.homeTeam} vs {self.awayTeam}",
            "full_time_score":f"{self.homeGoals}-{self.awayGoals}",
            "referee":f"{self.referee}",
            "winner":winner,
            "match_date":self.date_played,
            "recorded_dateTime":self.dateCreated
        }
        
