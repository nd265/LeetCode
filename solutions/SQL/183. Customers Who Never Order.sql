-- 183. Customers Who Never Order (https://leetcode.com/problems/customers-who-never-order/)
-- author: Navya Dahiya
-- created: 02 Jan, 2022


select c.name as Customers from Customers c 
left join 
Orders o
on c.id=o.customerId
where o.customerId is null