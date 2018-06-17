SELECT city_data.year, city_data.avg_temp AS avg_temp_tokyo, global_data.avg_temp AS avg_temp_global
FROM city_data, global_data
WHERE (city_data.year = global_data.year) AND NOT (city_data.avg_temp IS NULL) AND (city_data.city = 'Tokyo');