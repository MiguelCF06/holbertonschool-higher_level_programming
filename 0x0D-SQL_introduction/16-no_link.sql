-- Lists all records of the second_table of hbtn_0c_0
SELECT score, name FROM second_table WHERE name IS NOT NULL and name != ''
ORDER BY score DESC;
