-- lists all shows from db with their rating
-- db name will be passed as an arg to mysql command
SELECT title, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_shows
LEFT OUTER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;