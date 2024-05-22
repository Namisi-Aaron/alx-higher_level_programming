-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT b.name, COUNT(b.name) AS number_of_shows
FROM tv_shows a, tv_genres b, tv_show_genres c
WHERE a.id = c.show_id AND b.id = c.genre_id
GROUP BY b.name
ORDER BY number_of_shows DESC;
