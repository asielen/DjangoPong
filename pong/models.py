from django.db import models
# from datetime import datetime
# from django.core.serializers.json import DjangoJSONEncoder

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    name_short = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    player_1A = models.ForeignKey(Player,
                                  on_delete='SET_NULL',
                                  related_name='player_1A_set')
    player_1B = models.ForeignKey(Player,
                                  on_delete='SET_NULL',
                                  related_name='player_1B_set',
                                  blank=True,
                                  null=True)
    player_2A = models.ForeignKey(Player,
                                  on_delete='SET_NULL',
                                  related_name='player_2A_set')
    player_2B = models.ForeignKey(Player,
                                  on_delete='SET_NULL',
                                  related_name='player_2B_set',
                                  blank=True,
                                  null=True)
    team_1_Score = models.IntegerField(default=21)
    team_2_Score = models.IntegerField(default=21)
    match_date = models.DateTimeField('match date')
    window_team = models.IntegerField(default=1,blank=True,null=True)
    starting_team = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return '{} {} v {} {}'.format(self.player_1A, self.player_1B, self.player_2A, self.player_2B)

    @property
    def number_of_players(self):
        val = 2
        if self.player_1B: val += 1
        if self.player_2B: val += 1
        return val

    @property
    def point_difference(self):
        return abs(self.team_1_Score-self.team_2_Score)

    @property
    def winning_team(self):
        if self.team_1_Score>self.team_2_Score:
            return 1
        elif self.team_1_Score<self.team_2_Score:
            return 2
        else:
            return None

    @property
    def google_sheets_format(self):
        #HEADER_ROW = ['Team 1 Player 1 (1)', 'Team 1 Player 2 (3)', 'Team 2 Player 1 (2)', 'Team 2 Player 2 (4)', 'Team 1 Score', 'Team 2 Score', 'Datetime', 'Diff/Split', 'Winning Team', 'Window Team', 'Starting Position']
        row = [
            str(self.player_1A),
            str(self.player_1B if self.player_1B else ''),
            str(self.player_2A),
            str(self.player_2B if self.player_2B else ''),
            self.team_1_Score,
            self.team_2_Score,
            self.match_date.strftime("%m/%d/%Y %H:%M:%S"),
            self.point_difference,
            self.winning_team,
            self.window_team,
            self.starting_team
        ]
        return row
