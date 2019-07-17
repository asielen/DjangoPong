# https://steemit.com/utopian-io/@steempytutorials/part-3-combing-charts-js-and-django-rest-framework
from django.db import connection, transaction

def get_games_per_player():
    sql = """
    SELECT name, strftime('%Y-%m-%d',match_date) as date, COUNT(*) as games
FROM (
         SELECT *
         FROM (SELECT player_1A_id as player, team_1_Score as team_score, team_2_Score as opponent_score, CASE WHEN team_1_Score>team_2_Score THEN 1 ELSE 0 END player_win, match_date
               FROM pong_match
               UNION ALL
               SELECT player_1B_id as player, team_1_Score as team_score, team_2_Score as opponent_score, CASE WHEN team_1_Score>team_2_Score THEN 1 ELSE 0 END player_win, match_date
               FROM pong_match
               UNION ALL
               SELECT player_2A_id as player, team_2_Score as team_score, team_1_Score as opponent_score, CASE WHEN team_2_Score>team_1_Score THEN 1 ELSE 0 END player_win, match_date
               FROM pong_match
               UNION ALL
               SELECT player_2B_id as player, team_2_Score as team_score, team_1_Score as opponent_score, CASE WHEN team_2_Score>team_1_Score THEN 1 ELSE 0 END player_win, match_date
               FROM pong_match
              )
                  JOIN pong_player ON player = pong_player.id
     )
GROUP BY 1,2
    """
    data = raw_sql_query(sql)
    parsed_data = {}
    for d in data:
        # Parse the dics into separate dics per person
        if d['name'] not in parsed_data:
            parsed_data[d['name']] = []
        parsed_data[d['name']].append({'x':d['date'], 'y':d['games']})
    return parsed_data


def raw_sql_query(sql):
    results = None
    with connection.cursor() as cursor:

        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        results = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return results