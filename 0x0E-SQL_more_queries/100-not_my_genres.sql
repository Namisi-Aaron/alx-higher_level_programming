-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT x.name
FROM tv_genres x
WHERE x.name NOT IN
(
SELECT DISTINCT name
FROM tv_shows a
LEFT JOIN tv_show_genres b ON a.id = b.show_id
LEFT JOIN tv_genres c ON b.genre_id = c.id
WHERE a.title = 'Dexter'
)
ORDER BY x.name ASC;
