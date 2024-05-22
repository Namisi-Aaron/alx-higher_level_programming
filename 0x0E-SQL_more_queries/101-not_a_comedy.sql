-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT title
FROM tv_shows
WHERE title NOT IN
(
SELECT title
FROM tv_shows a
LEFT JOIN tv_show_genres b ON a.id = b.show_id
LEFT JOIN tv_genres c ON b.genre_id = c.id
WHERE name = 'Comedy'
)
ORDER BY title ASC;
