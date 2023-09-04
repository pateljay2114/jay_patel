create database Worker_details ;
use Worker_details ;
select * from Worker ;

/* Q-1 Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME 
Ascending and DEPARTMENT Descending. */

select * from worker order by FIRST_NAME asc ;

select * from worker order by DEPARTMENT desc ;

/* Q-2 Write an SQL query to print details for Workers with the first names “Vipul” and “Satish” 
from the Worker table. */

select * from worker where FIRST_NAME = "Vipul" ;

select * from worker where FIRST_NAME = "Satish" ;

select * from worker where FIRST_NAME = "Vipul" or FIRST_NAME = "Satish" ;

/* Q-3 Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and 
contains six alphabets */

select * from worker where FIRST_NAME like '_%_%_%_%_h%' ;

/* Q-4 Write an SQL query to print details of the Workers whose SALARY lies between 1. */

select * from worker where SALARY between 0 and 100000 ;

/* Q-5 Write an SQL query to fetch duplicate records having matching data in some fields of a table. */




/* Q-6 Write an SQL query to show the top 6 records of a table.  */

select * from worker limit 6 ;

/* Q-7 Write an SQL query to fetch the departments that have less than five people in them. */

select count(WORKER_ID) , DEPARTMENT from worker group by DEPARTMENT having count(WORKER_ID) < 5 ;

/* Q-8 Write an SQL query to show all departments along with the number of people in there. */

select count(WORKER_ID) , DEPARTMENT from worker group by DEPARTMENT having count(WORKER_ID) ;

/* Q-9 Write an SQL query to print the name of employees having the highest salary in each 
department. */

select max(SALARY) from worker ;




create database school ;
use school ;

/* Q-1 To display all the records form STUDENT table. SELECT * FROM student */

select * from student ;

/* Q-2 To display any name and date of birth from the table */

select Std_Name , DOB from student ;

/* Q-3 To display all students record where percentage is greater of equal to 80. */
 
select * from student where percentage >= 80 ;

/* Q-4  To display student name, stream and percentage where percentage of student is more than 80. */

select Std_Name, Stream, Percentage from student where Percentage > 80;

/* Q-5 To display all records of science students whose percentage is more than 75 form student table. */

select * from student where Stream = 'Science' and Percentage > 75 ;