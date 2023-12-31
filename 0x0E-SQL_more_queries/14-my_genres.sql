-- lists all genres of the show Dexter
-- db passed as argument of the mysql command
SELECT name
FROM tv_genres
LEFT OUTER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT OUTER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;