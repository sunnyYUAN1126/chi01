#新增資料 insert into...set/value
insert into cmdev.dept
set deptno=100,dname="Delivery";

insert into cmdev.emp
values(8001,"MILLER","CLERK",7782,"1982-01-23",1300,null,10),
	  (8002,"MILLER","CLERK",7782,"1982-01-23",1300,null,50),
      (8003,"MILLER","CLERK",7782,"1982-01-23",1300,null,50);
-----------------------------------------------------
#更新資料
replace into cmdev.emp
values(8001,"MILLER","CLERK",7782,"1982-01-23",1300,null,50);

update cmdev.emp
set deptno=90
where deptno=50 and empno=8001;

-----------------------------------------
update cmdev.emp
set salary=salary+100
limit 3;
update cmdev.emp
set salary=salary+100
order by salary
limit 3;

update cmdev.emp
set salary=salary+100
order by salary desc
limit 3;
---------------------
#刪除資料
delete from cmdev.emp
where empno in(8001,8002,8003);

-------------------
#創建一個資料庫 & 刪除資料庫
CREATE DATABASE employeeDB
CHARACTER SET big5
COLLATE big5_chinese_ci;

show databases;

drop database if exists employeeDB;
-------------------------- 
#新增資料表
use employeeDB;
create table EMPLOYEE(
	ID int not null,
    FirstName varchar(40) not null,
    LastNameemployee varchar(40) not null,
    Birthday date,
    Salary float,
    primary key(ID)
);

#新增資料
insert into employee values (1001,"Troy","Hammer","1965-03-31",102109.15);
insert into employee values (1002,"Michaek","Walton","1989-04-01",9000.0);
insert into employee values (1003,"Jsdaf","Dggrds","1985-10-15",232109.6);