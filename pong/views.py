import random

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import Player, Match
from .forms import MatchSubmit
from .google_sheets import update_rakings_sheet



# Create your views here.

def index(request):
    return render(request, 'pong/index.html')

def submit_match(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MatchSubmit(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = form.save(commit=False)
            obj.match_date = timezone.localtime()
            obj.save()
            # Update google sheet
            update_rakings_sheet(obj.google_sheets_format)

            if 'Submit and Swap' in request.POST:
                initial = {'player_1A':obj.player_2A.id if obj.player_2A else None,
                           'player_1B':obj.player_2B.id if obj.player_2B else None,
                           'player_2A':obj.player_1A.id if obj.player_1A else None,
                           'player_2B':obj.player_1B.id if obj.player_1B else None,
                           'starting_team':obj.starting_team
                           }
            if 'Submit and Rotate' in request.POST:
                players = [obj.player_1A, obj.player_1B, obj.player_2A, obj.player_2B]
                players = [p.id for p in players if p]
                if len(players) == 2:
                    initial = {'player_1A': players[1],
                               'player_2A': players[0],
                               }
                elif len(players) == 3:
                    if not obj.player_2B: # No 2B/3
                        # 0,1,2,3 -> 0,1,2,3 -> 0,1,2,3 Positions
                        # 0,1,2,# -> #,0,1,2 -> 0,#,1,2  Shift
                        # 0,1,2,# -> #,0,1,2 -> 0,#,1,2  List Elements
                        initial = {'player_1A': obj.player_1A.id if obj.player_1A else None,
                                   'player_1B': None,
                                   'player_2A': obj.player_1B.id if obj.player_1B else None,
                                   'player_2B': obj.player_2A.id if obj.player_2A else None,
                                   'starting_team': obj.starting_team
                                   }

                    else: # No 1B/1
                        # 0,1,2,3 -> 0,1,2,3 -> 0,1,2,3 Positions
                        # 0,#,2,3 -> 3,0,#,2 -> 3,0,2,#  Shift
                        # 0,#,1,2 -> 2,0,#,1 -> 2,0,1,#  List Elements
                        initial = {'player_1A':obj.player_2A.id if obj.player_2A else None,
                                   'player_1B':obj.player_1A.id if obj.player_1A else None,
                                   'player_2A':obj.player_2B.id if obj.player_2B else None,
                                   'player_2B': None,
                                   'starting_team':obj.starting_team
                                   }
                else:
                    initial = {'player_1A': obj.player_2B.id if obj.player_2B else None,
                               'player_1B': obj.player_1A.id if obj.player_1A else None,
                               'player_2A': obj.player_1B.id if obj.player_1B else None,
                               'player_2B': obj.player_2A.id if obj.player_2A else None,
                               'starting_team': obj.starting_team
                               }
            elif 'Submit and Shuffle' in request.POST:
                players = [obj.player_1A,obj.player_1B,obj.player_2A,obj.player_2B]
                random.shuffle([p.id for p in players if p])
                initial = {'player_1A': players[0],
                           'player_2A': players[1],
                           }
                if len(players)>=3:
                    initial['player_1B']=players[2]
                    if len(players) == 4:
                        initial['player_2B'] = players[3]
            else:
                initial = {'player_1A': obj.player_1A.id if obj.player_1A else None,
                           'player_1B': obj.player_1B.id if obj.player_1B else None,
                           'player_2A': obj.player_2A.id if obj.player_2A else None,
                           'player_2B': obj.player_2B.id if obj.player_2B else None,
                           'starting_team': 1 if obj.starting_team == 2 else 2
                           }
            form = MatchSubmit(initial=initial)

            # Rerender form with new values
            return render(request, 'pong/submit_match.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MatchSubmit(initial={'starting_team':2})

    return render(request, 'pong/submit_match.html', {'form': form})

def user_stats(request, user_name):
    user = Player.objects.get(name=user_name)
    return HttpResponse("Hi {}".format(user.name))

def all_matches(request):
    matches = Match.objects.order_by('match_date')
    context = {'matches_list': matches}
    return render(request, 'pong/matches_list.html', context)

