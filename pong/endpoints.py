
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
from .reports import get_games_per_player

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "data": [12, 19, 3, 5, 2, 3, 10],
        }

        return Response(data)

class Rankings(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # players = ['1A','1B','2A','2B']
        # data = {}
        # for p in players:
        #     data[p] = Match.objects\
        #         .filter(**{'player_{}__isnull'.format(p):False})\
        #         .annotate(day=TruncDay('match_date'))\
        #         .values('day','player_{}__name'.format(p))\
        #         .annotate(created_count=Count('id'))
        data = get_games_per_player()
        return Response(data)



