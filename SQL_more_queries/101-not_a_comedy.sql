-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT tv_shows.title
FROM hbtn_0d_tvshows.tv_shows
INNER JOIN hbtn_0d_tvshows.tv_show_genres
ON tv_shows.id = tv_show_genres.show_id 
INNER JOIN hbtn_0d_tvshows.tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name != "Comdey"
ORDER BY tv_shows.title;
