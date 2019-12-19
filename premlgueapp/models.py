from django.db import models

class Overview(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    matches_played = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    league_position = models.IntegerField()
    goals_scored = models.IntegerField()
    goals_conceded = models.IntegerField()
    goal_difference = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        db_table = "overview"