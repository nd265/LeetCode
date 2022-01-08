-- 175. Combine Two Tables (https://leetcode.com/problems/combine-two-tables/)
-- author: Navya Dahiya
-- created: 3 Jan, 2022

select  p.firstName, 
        p.lastname,
        a.city, 
        a.state
        from Person p
        left join Address a
        on p.personId = a.personId
       