-- Displays the average temperature (Fahrenheit) by city
SELECT t.city, AVG(t.value) avg_temp
FROM temperatures t
GROUP BY t.city
ORDER BY avg_temp DESC;
