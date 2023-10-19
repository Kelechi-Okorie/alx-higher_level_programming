-- lists only the comedy in the db
-- db name will be passed as an arg to mysql command
SELECT title
FROM tv_shows
LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;
