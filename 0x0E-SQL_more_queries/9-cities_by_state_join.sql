-- This script filters TABLES using JOIN
SELECT cities.id, cities.name, states.name FROM cities c
INNER JOIN states s
-- ON cities.state_id = states.id
ORDER BY cities.id;
