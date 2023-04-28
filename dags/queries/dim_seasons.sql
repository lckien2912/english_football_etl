SELECT
    season_id,
    season,
    tier,
    division,
    (
        SELECT t.team_id 
        FROM `future-glider-383316.staging_football_dataset.staging_teams` AS t
        WHERE t.team_name = s.winner
    ) AS winner,
    count_teams
FROM `future-glider-383316.staging_football_dataset.staging_seasons` AS s;