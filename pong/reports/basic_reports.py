# https://steemit.com/utopian-io/@steempytutorials/part-3-combing-charts-js-and-django-rest-framework
from django.db import connection, transaction

def get_all_games(startdate=None, enddate=None, players=None):
    sql = """
    SELECT m.id, p1.name Player_1A, p2.name Player_1B, p3.name Player_2A, p4.name Player_2B, team_1_Score, team_2_Score, window_team, starting_team, match_date FROM pong_match m
        JOIN pong_player p1 ON player_1A_id = p1.id
        JOIN pong_player p2 ON player_1B_id = p2.id
        JOIN pong_player p3 ON player_2A_id = p3.id
        JOIN pong_player p4 ON player_2B_id = p4.id
        WHERE match_date >= %s AND match_date < %s;
    """
    if not startdate:
        startdate = '2019-01-01'
    if not enddate:
        enddate = '2050-01-01'
    data = raw_sql_query(sql, (startdate, enddate))
    return data

def get_games_per_player():
    sql = """WITH flattable AS (
    SELECT * FROM
        (SELECT player_1A_id as player, team_1_Score as team_score, team_2_Score as opponent_score, CASE WHEN team_1_Score>team_2_Score THEN 1 ELSE 0 END player_win, match_date
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
),
match_counts AS (
    SELECT name,
           strftime('%Y-%m-%d', match_date) as date,
           COUNT(*) as d_games
    FROM flattable
             JOIN pong_player ON player = pong_player.id
    GROUP BY 1, 2 ORDER BY 1,2
)
SELECT * FROM match_counts"""
    data = raw_sql_query(sql)
    parsed_data = {}
    for d in data:
        # Parse the dics into separate dics per person
        if d['name'] not in parsed_data:
            parsed_data[d['name']] = []
        parsed_data[d['name']].append({'x':d['date'], 'y':d['d_games']})
    return parsed_data

#SUM(d_games) OVER (partition by name ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as c_games
#SUM(COUNT(*)) OVER(partition by name ORDER BY match_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as c_games


def raw_sql_query(sql, injection = None):
    results = None
    with connection.cursor() as cursor:

        if injection:
            cursor.execute(sql, injection)
        else:
            cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        results = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return results