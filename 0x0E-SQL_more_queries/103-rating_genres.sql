-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT name, SUM(rate) rating
FROM tv_show_ratings a, tv_shows b, tv_show_genres c, tv_genres d
WHERE a.show_id = b.id
AND d.id = c.genre_id
AND b.id = c.show_id
GROUP BY name
ORDER BY rating DESC;
