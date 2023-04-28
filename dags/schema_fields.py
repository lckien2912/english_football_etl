TEAM_SCHEMA_FIELDS = [
    {'name': 'key_id', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'team_id', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'team_name', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'former_team_names', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'current', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'former', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'defunct', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'first_appearance', 'type': 'STRING', 'mode': 'REQUIRED'},
]

SEASON_SCHEMA_FIELDS = [
    {'name': 'key_id', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'season_id', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'season', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'tier', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'division', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'subdivision', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'winner', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'count_teams', 'type': 'INT64', 'mode': 'REQUIRED'},
]

STANDING_SCHEMA_FIELDS = [
    {'name': 'key_id', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'season_id', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'season', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'tier', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'division', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'subdivision', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'position', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'team_id', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'team_name', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'played', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'wins', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'draws', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'losses', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'goals_for', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'goals_against', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'goal_difference', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'points', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'point_adjustment', 'type': 'INT64', 'mode': 'REQUIRED'},
]

MATCH_SCHEMA_FIELDS = [
    {'name': 'key_id', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'season_id', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'season', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'tier', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'division', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'subdivision', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'match_id', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'match_name', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'home_team_id', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'home_team_name', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'away_team_id', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'away_team_name', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'score', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'home_team_score', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'away_team_score', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'home_team_score_margin', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'away_team_score_margin', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'result', 'type': 'STRING', 'mode': 'REQUIRED'},
    {'name': 'home_team_win', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'away_team_win', 'type': 'INT64', 'mode': 'REQUIRED'},
    {'name': 'draw', 'type': 'INT64', 'mode': 'REQUIRED'}
]