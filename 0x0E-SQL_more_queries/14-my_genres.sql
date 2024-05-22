-- luses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT b.name
FROM tv_shows a, tv_genres b, tv_show_genres c
WHERE a.id = c.show_id AND b.id = c.genre_id AND a.title = 'Dexter'
ORDER BY b.name;
