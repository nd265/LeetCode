-- 197. Rising Temperature (https://leetcode.com/problems/rising-temperature/)
-- auhtor: Navya Dahiya
-- created: 02 Jan, 2022

select
    weather.id AS 'Id'
from
    weather
        join
    weather w ON DATEDIFF(weather.recordDate, w.recordDate) = 1
        AND weather.Temperature > w.Temperature