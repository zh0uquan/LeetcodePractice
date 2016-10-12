# Write your MySQL query statement below
DELETE p2 FROM Person AS p1, Person as p2 where p1.email = p2.email AND p2.id > p1.id;