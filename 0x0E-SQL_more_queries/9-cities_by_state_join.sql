-- lists all cities contained in the db
-- db name will be passed to the mysql command
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id