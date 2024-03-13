-- Import in hbtn_0c_0 database
-- into a temperature dump

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
