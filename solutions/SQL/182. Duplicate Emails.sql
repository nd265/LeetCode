-- 182. Duplicate Emails (https://leetcode.com/problems/duplicate-emails/)
-- auhtor: Navya Dahiya
-- created: 02 Jan, 2022

select email from Person
group by email
having count(*)>1