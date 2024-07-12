-- https://leetcode.com/problems/rising-temperature

select w2.id
from Weather w1 
join Weather w2
on DATEDIFF(w1.recordDate, w2.recordDate) = -1 AND w1.temperature < w2.temperature 
