-- lists all cities of california
-- db name passed as argument
SELECT id, name FROM cities WHERE stat_id = (SELECT id FROM states WHERE name =     `California`) ORDER BY id ASC