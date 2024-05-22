-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT a.title
FROM tv_shows a, tv_genres b, tv_show_genres c
WHERE a.id = c.show_id AND b.id = c.genre_id AND b.name = 'Comedy'
ORDER BY a.title;
