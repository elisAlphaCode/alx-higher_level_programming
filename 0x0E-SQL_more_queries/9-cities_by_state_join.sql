-- Lists all cities in the database hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id.

SELECT cities.id, cities.name, cities.name
FROM cities
INNER JOIN states ON cities.id = states.id
ORDER BY cities.id;
