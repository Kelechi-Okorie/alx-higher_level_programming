-- lists all genres in the db
-- db name will be passed as an argument
SELECT tv_genres.name, SUM(tv_ratings.rate) AS 'rating'
FROM tv_genres
INNER JOIN tv_show_genres On tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY name ASC;