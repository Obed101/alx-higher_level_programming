-- This script does it all
SELECT ts.title, tg.genre_id FROM tv_shows tg
LEFT JOIN tv_show_genres ts
ON tg.title = tg.genre_id OR tg.show_id = NULL
ORDER BY ts.title, tg.genre_id ASC;
