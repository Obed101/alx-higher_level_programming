-- This script does it all
SELECT ts.title, tg.genre_id FROM tv_shows ts
INNER JOIN tv_show_genres tg
ON ts.show_id = tg.genre_id
ORDER BY ts.title, tg.genre_id ASC;
