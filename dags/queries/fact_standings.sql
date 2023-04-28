SELECT 
    season_id,
    team_id,
    tier,
    played,
    position,
    wins,
    draws,
    losses,
    points
FROM `future-glider-383316.staging_football_dataset.staging_standings`
ORDER BY season_id, position;