# https://steemit.com/utopian-io/@steempytutorials/part-3-combing-charts-js-and-django-rest-framework
from .report_helper import raw_sql_query

def get_players():
    sql = """
        SELECT id, name, name_short FROM pong_player
        """
    data = raw_sql_query(sql)
    return data

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
    sql = """SELECT p1.name as player, team_score, opponent_score, player_win, match_date, match_id FROM
        (SELECT  id as match_id, player_1A_id as player, team_1_Score as team_score, team_2_Score as opponent_score, CASE WHEN team_1_Score>team_2_Score THEN 1 ELSE 0 END player_win, match_date
            FROM pong_match
            UNION ALL
            SELECT  id as match_id, player_1B_id as player, team_1_Score as team_score, team_2_Score as opponent_score, CASE WHEN team_1_Score>team_2_Score THEN 1 ELSE 0 END player_win, match_date
            FROM pong_match
            UNION ALL
            SELECT  id as match_id, player_2A_id as player, team_2_Score as team_score, team_1_Score as opponent_score, CASE WHEN team_2_Score>team_1_Score THEN 1 ELSE 0 END player_win, match_date
            FROM pong_match
            UNION ALL
            SELECT  id as match_id, player_2B_id as player, team_2_Score as team_score, team_1_Score as opponent_score, CASE WHEN team_2_Score>team_1_Score THEN 1 ELSE 0 END player_win, match_date
            FROM pong_match
        ) as p0
            JOIN pong_player as p1 ON player = p1.id"""
    data = raw_sql_query(sql)
    parsed_data = {}
    # for d in data:
    #     # Parse the dics into separate dics per person
    #     if d['player'] not in parsed_data:
    #         parsed_data[d['player']] = []
    #     parsed_data[d['player']].append({'x':d['date'], 'y':d['d_games']})
    return data

def get_games_per_team():
    sql = """SELECT p1.name as player1, p2.name as player2, team_score, opponent_score, team_win, score_diff match_date, match_id FROM
        (SELECT id as match_id, player_1A_id as player1, player_1B_id as player2, team_1_Score as team_score, team_2_Score as opponent_score, CASE WHEN team_1_Score>team_2_Score THEN 1 ELSE 0 END team_win, team_1_Score-team_2_Score as score_diff, match_date
            FROM pong_match
            UNION ALL
            SELECT id as match_id, player_2A_id as player1, player_2B_id as player2, team_2_Score as team_score, team_1_Score as opponent_score, CASE WHEN team_2_Score>team_1_Score THEN 1 ELSE 0 END team_win, team_2_Score-team_1_Score as score_diff, match_date
            FROM pong_match
        )
            JOIN pong_player as p1 ON player1 = p1.id
            JOIN pong_player as p2 ON player2 = p2.id"""
    data = raw_sql_query(sql)
    parsed_data = {}
    # for d in data:
    #     # Parse the dics into separate dics per person
    #     if d['player1']+d['player2'] not in parsed_data:
    #         parsed_data[d['name']] = []
    #     parsed_data[d['name']].append({'x':d['date'], 'y':d['d_games']})
    return data

#SUM(d_games) OVER (partition by name ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as c_games
#SUM(COUNT(*)) OVER(partition by name ORDER BY match_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as c_games


def get_player_stats_daily():
    sql="""
WITH flattable AS (
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
           COUNT(*) as d_games,
    FROM flattable
             JOIN pong_player ON player = pong_player.id
    GROUP BY 1, 2 ORDER BY 1,2
)
SELECT * FROM match_counts"""
    data = raw_sql_query(sql)
    return data
