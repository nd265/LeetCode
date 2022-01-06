-- 596. Classes More Than 5 Students (https://leetcode.com/problems/classes-more-than-5-students)
-- author: Navya Dahiya
-- created: 02 Jan, 2022

select class from Courses
group by class
having count(*) >=5;