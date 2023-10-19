-- lists all genres in the db
-- db name will be passed as an argument
SELECT name, SUM(tv_ratings.rate) AS 'rating'
FROM tv_genres
LEFT OUTER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT OUTER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY name ASC;