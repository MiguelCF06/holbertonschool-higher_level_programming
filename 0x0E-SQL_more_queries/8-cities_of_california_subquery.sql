-- Lists all the cities of California that can be found in the database.
-- The states table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
-- Not allowed to use the JOIN keyword
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE
name = 'California') ORDER BY id;
