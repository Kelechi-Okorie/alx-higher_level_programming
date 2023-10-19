-- displays the average temperature(Fahrenheit) by city
-- ordered by temperature(descreasing)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY city DESC;