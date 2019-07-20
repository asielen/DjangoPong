
from django.db.models import (
    Count,
    Avg,
    Sum,
    Case,
    When,
    Value,
    IntegerField,
)
from django.db.models.functions import (TruncDay,Concat,)


from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Player, Match
from .reports import get_games_per_player, get_all_games

class All(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        stardate = self.request.query_params.get('startdate', None)
        enddate = self.request.query_params.get('enddate', None)
        players = self.request.query_params.get('players', None)

        data = get_all_games(stardate, enddate, players)
        return Response(data)

class Rankings(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = get_games_per_player()
        return Response(data)



