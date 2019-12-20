from django.db import models

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    team_id = models.IntegerField()
    player_name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    min_played_home = models.IntegerField()
    nationality = models.CharField(max_length=100)
    appearances = models.IntegerField()
    goals_total = models.IntegerField()
    overall_assists = models.IntegerField()
    penalty_goals = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    class Meta:
        db_table = "player"
