SELECT Continent,Region,sum(Population)
FROM world.country
group by Continent,Region 
order by Continent,sum(Population) ;

SELECT Region,sum(Population) as sumPop
FROM world.country
where Continent in("Asia")
group by Region
order by sumPop;


SELECT Region,sum(Population) as sumPop
FROM world.country
group by Region
having sumPop>100000000
order by sumPop;
------

SELECT country.Name as "國家名稱",
	   country.Population as "總人口數",
       city.Name as "首都",
       city.Population as "首都人口"
FROM world.country,world.city
where Capital=ID;

-----------------
use cmdev;
SELECT empno,ename,dname 
FROM emp INNER JOIN dept
using (deptno);
#on emp.deptno=dept.deptno; 或是用on




