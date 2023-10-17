-- lists number of record with same score in second_table
-- the result should display the number of records for this score
SELECT score, COUNT(score) 'number' FROM second_table GROUP BY score ORDER BY number DESC;