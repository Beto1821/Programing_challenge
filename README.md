# Database Challenge - Support Engineer

## Challenge:
The challenge was to create a table called 'AverageLifeExpectancy' with the information from the 'World' database (https://dev.mysql.com/doc/index-other.html). The new table created should have the average life expectancy from three regions: South America, North America and Asia.

## Process:
To accomplish this challenge, I utilized the SGBD DBeaver to analyze the data, create the table, and export the required database.

I found the 'Life Expectancy' and 'Continent' columns at the country table with the query: 
```sql
SELECT * FROM world.country;
```
## Query: 
```sql
CREATE TABLE AverageLifeExpectancy AS
SELECT ROUND(AVG(LifeExpectancy)) AS LifeProm, Continent AS Region
FROM world.country
WHERE Continent IN ('South America', 'North America', 'Asia')
GROUP BY Continent
ORDER BY Continent DESC;
```
#### Explanation:

+ Selected the 'LifeExpectancy' and 'Continent' columns, renaming them to 'LifeProm' and 'Region', respectively. Utilized ```AVG()``` inside ```ROUND()``` to get the average value of 'LifeExpectancy' without decimals:
     ```sql
    SELECT ROUND(AVG(LifeExpectancy)) AS LifeProm, Continent AS Region
    ```
+ Chose the 'world.country' table from the 'world' database:
     ```sql
    FROM world.country
    ```
+ Used the ```WHERE``` clause to filter the data to only include countries from the three specific continents:
     ```sql
    WHERE Continent IN ('South America', 'North America', 'Asia')
    ```
+ Employed the ```GROUP BY``` clause to group the data by continent:
     ```sql
    GROUP BY Continent
    ```
+ Utilized the ```ORDER BY`` clause to sort the results in descending order based on the continent:
     ```sql
    ORDER BY Continent DESC
    ```
+ Used the ```CREATE TABLE``` arguments for create the new table with the correct data with the name of 'AverageLifeExpectancy':
     ```sql
    CREATE TABLE AverageLifeExpectancy AS
    ```
## Results:
Total countries: 239
Countries in the specified continents: 102
Valid values (not null) for 'LifeExpectancy' column: 101

The resulting table displays the average life expectancy for each requested continent:
| LifeProm |     Region    |
|----------|---------------|
|    71    | South America |
|    73    | North America |
|    67    |      Asia     |


North America has the highest life expectancy of 73 years, followed by South America with 71 years, and Asia with the lowest at 67 years.
