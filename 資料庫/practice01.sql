use world;

select id,name
from city;

select 10*10 as 計算;

select  ename as "select",
		salary as "month salary",
		salary*12 as "Annual Salary",
		(salary*12+salary div 2) as "full Salary"
from cmdev.emp;

select name,capital,Population
from world.country
where continent="Asia" and   Population > 50000000;

select *
from world.countrylanguage
where Language like "%Chinese%" AND IsOfficial="T";
 


