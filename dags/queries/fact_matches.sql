SELECT 
    match_id,
    match_name,
    home_team_id,
    away_team_id,
    home_team_score,
    away_team_score,
    home_team_score_margin,
    away_team_score_margin,
    home_team_win,
    away_team_win,
    draw
FROM `future-glider-383316.staging_football_dataset.staging_matches`
ORDER BY match_id;