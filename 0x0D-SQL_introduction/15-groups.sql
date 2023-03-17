-- list tables of databases
-- calculates grouped scores
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
