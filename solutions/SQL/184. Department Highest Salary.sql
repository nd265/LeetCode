-- 184. Department Highest Salary (https://leetcode.com/problems/department-highest-salary/)
-- author: Navya Dahiya
-- created: 8 Jan, 2022

SELECT 
    d.name as Department, e.name as Employee, e.salary as Salary
    FROM Department d 
    JOIN Employee e
    ON d.id = e.departmentId
    WHERE(d.id, e.salary) IN (
SELECT 
    departmentId, MAX(salary)
    FROM 
        Employee
    GROUP BY departmentId
    )
