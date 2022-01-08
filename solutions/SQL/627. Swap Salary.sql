-- 627. Swap Salary (https://leetcode.com/problems/swap-salary/)
-- author: Navya Dahiya
-- created: 8 Jan, 2022

UPDATE Salary
SET sex = CASE 
        WHEN sex = 'm' THEN 'f'
        WHEN sex = 'f' THEN 'm'
        END
