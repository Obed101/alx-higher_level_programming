-- This script filters TABLES using JOIN
SELECT cities.id, cities.name, states.name FROM cities c
INNER JOIN states s
ON c.state_id = s.id
ORDER BY cities.id;
