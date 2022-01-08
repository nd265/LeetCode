-- 181. Employees Earning More Than Their Managers (https://leetcode.com/problems/employees-earning-more-than-their-managers/)
-- author: Navya Dahiya
-- created: 2 Jan, 2022

select e.name as Employee from Employee e
where e.salary > (select salary from Employee where e.managerId=id)
