-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT title, SUM(rate) rating
FROM tv_show_ratings a, tv_shows b
WHERE a.show_id = b.id
GROUP BY title
ORDER BY rating DESC;
