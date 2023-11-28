-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
SELECT DISTINCT tv_genres.name
FROM hbtn_0d_tvshows.tv_genres
INNER JOIN hbtn_0d_tvshows.tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id 
WHERE NOT (tv_show_genres.show_id = (SELECT id FROM hbtn_0d_tvshows.tv_shows WHERE title = "Dexter"))
ORDER BY tv_genres.name;
