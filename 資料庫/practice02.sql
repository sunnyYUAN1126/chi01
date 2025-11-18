SELECT CountryCode,Name
FROM world.city
order by CountryCode,Name ;

SELECT CountryCode,Name
FROM world.city
order by CountryCode asc,Name desc;

SELECT ename,salary,salary*12 as yearsalary
FROM cmdev.emp
order by 3;
#選第三個欄位排序

----------------------------- 
SELECT empno,ename,salary
FROM cmdev.emp
order by salary
limit 3;

SELECT empno,ename,salary
FROM cmdev.emp
order by salary desc
limit 3;

SELECT Name,CountryCode,Population 
FROM world.city
where Population>8000000
order by Population desc
limit 6;

#排除重複資料 DISTINCT
SELECT DISTINCT Continent 
FROM world.country;
----------------------------

select @@sql_mode;
select "fds"+"sf";
----------------------

SELECT name,LENGTH(Name) as "Name length"
FROM world.country
order by LENGTH(Name) desc
limit 5;

SELECT ename, hiredate,  datediff(CURDATE(),hiredate)
FROM cmdev.emp;



