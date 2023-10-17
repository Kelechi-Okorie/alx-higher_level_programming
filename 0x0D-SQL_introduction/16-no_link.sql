-- lists all records of the table second_table
-- results should display the score and the name in this order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;