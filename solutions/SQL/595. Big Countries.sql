-- 595. Big Countries (https://leetcode.com/problems/big-countries/)
-- author: Navya Dahiya
-- created: 02 Jan, 2022

select name, 
        population, 
        area 
            from 
        World
            where
                area >= 3000000
                    or
                population >= 25000000