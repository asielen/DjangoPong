from django import forms

from .models import Match

class MatchSubmit(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['player_1A',
                  'player_1B',
                  'player_2A',
                  'player_2B',
                  'team_1_Score',
                  'team_2_Score',
                  'starting_team']

    def clean(self):
        super(MatchSubmit, self).clean()
        # This method will set the `cleaned_data` attribute
        player_1A = self.cleaned_data.get('player_1A')
        player_1B = self.cleaned_data.get('player_1B')
        player_2A = self.cleaned_data.get('player_2A')
        player_2B = self.cleaned_data.get('player_2B')

        team_1_Score = self.cleaned_data.get('team_1_Score')
        team_2_Score = self.cleaned_data.get('team_2_Score')

        # Validate that 1A and 2A have players
        if not player_1A or not player_2A:
            # if not player_1A:
            #     self.add_error('player_1A','Please select a player 1A')
            # if not player_2A:
            #     self.add_error('player_2A','Please select a player 2A')
            raise forms.ValidationError('Must enter at least 2 player in position 1A and 2A')

        # Validate that there are no duplicate players
        players = [p for p in [player_1A, player_1B, player_2A, player_2B] if p != None]
        if len(players) != len(set(players)):
            # self.add_error(None,'There can not be duplicate players')
            # print("Duple Players Error")
            raise forms.ValidationError('There can not be duplicate players')

        # Validate there is a winner (no ties)
        if abs(team_1_Score-team_2_Score) < 2:
            # self.add_error('team_1_Score', 'Games must be won by at least 2 points')
            # print("Score Error")
            raise forms.ValidationError('Games must be won by at least 2 points')

