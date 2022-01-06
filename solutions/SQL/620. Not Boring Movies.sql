-- 620. Not Boring Movies (https://leetcode.com/problems/not-boring-movies/)
-- author: Navya Dahiya
-- created: 02 Jan, 2022

select * from Cinema 
    where
        id % 2 <> 0
        and 
        description <> 'boring'
    order by rating desc    
    