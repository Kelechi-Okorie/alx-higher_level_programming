-- lists all records with score >= 0 in second_table
-- should be ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;