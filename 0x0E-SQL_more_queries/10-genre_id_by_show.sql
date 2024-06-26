-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_genres, tv_show_genres
WHERE
tv_shows.id = tv_show_genres.show_id
AND tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
