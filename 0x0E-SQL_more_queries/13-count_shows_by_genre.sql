-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked
-- to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to
-- this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Dont display a genre that doesnt have any shows linked
SELECT tv_genres.name AS genres, COUNT(*) AS n_linshows FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id ORDER BY n_linshows DESC;
