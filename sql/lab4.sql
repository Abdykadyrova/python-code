SELECT * FROM city
    INNER JOIN country
    ON city.country_id = country.country_id
LIMIT 10;    