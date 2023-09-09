create database HR ;
use HR ;

select * from emp_data ;

-- Q1 :  Display all information in the tables EMP and DEPT.

select * from emp_data ;

-- Q2 : Display only the hire date and employee name for each employee. 

select FIRST_NAME , HIRE_DATE from emp_data ;

-- Q3 : Display the ename concatenated with the job ID, separated by a comma and space, and name the column Employee and Title 

select concat(FIRST_NAME,' , ',JOB_ID) as ' Employee_and_Title ' from emp_data ;

-- Q4 : Display the hire date, name and department number for all clerks.

select HIRE_DATE,FIRST_NAME,DEPARTMENT_ID from emp_data ;

-- Q5 : Create a query to display all the data from the EMP table. Separate each column by a comma. Name the column THE OUTPUT 

select emp_data.* , ' , ' as "the_output" from emp_data ;

-- Q6 : Display the names and salaries of all employees with a salary greater than 2000. 

select FIRST_NAME,SALARY from emp_data where SALARY > 2000 ;

-- Q7 : Display the names and dates of employees with the column headers "Name" and "Start Date"

select FIRST_NAME as Name ,
       HIRE_DATE as Start_Date from emp_data ;
       
-- Q8 : Display the names and hire dates of all employees in the order they were hired.   

select FIRST_NAME , HIRE_DATE from emp_data order by HIRE_DATE ;   

-- Q9 :  Display the names and salaries of all employees in reverse salary order. 

select  FIRST_NAME, SALARY from emp_data order by SALARY desc ;

-- Q10 : Display 'ename" and "deptno" who are all earned commission and display salary in reverse order.

select FIRST_NAME,DEPARTMENT_ID from emp_data WHERE COMMISSION_PCT IS NOT NULL
ORDER BY salary DESC;

-- Q11 :  Display the last name and job title of all employees who do not have a manager. 

SELECT LAST_NAME, JOB_ID
FROM emp_data
WHERE MANAGER_ID IS NULL;

-- Q12 : Display the last name, job, and salary for all employees whose job is sales representative 
--       or stock clerk and whose salary is not equal to $2,500, $3,500, or $5,000

SELECT LAST_NAME, JOB_ID, SALARY
FROM emp_data
WHERE (JOB_ID = 'sales representative' OR JOB_ID = 'stock clerk')
AND (SALARY NOT IN (2500, 3500, 5000));

SELECT LAST_NAME, JOB_ID, SALARY
FROM emp_data
WHERE (SALARY NOT IN (2500, 3500, 5000));



/* part - 2 */

-- Q1 :  Display the maximum, minimum and average salary and commission earned. 

SELECT 
    MAX(SALARY) AS max_salary,
    MIN(SALARY) AS min_salary,
    AVG(SALARY) AS avg_salary,
    MAX(COMMISSION_PCT) AS max_commission,
    MIN(COMMISSION_PCT) AS min_commission,
    AVG(COMMISSION_PCT) AS avg_commission
FROM emp_data ;


-- Q2 : Display the department number, total salary payout and total commission payout for each department. 

select DEPARTMENT_ID ,
sum(SALARY) as total_salary_payout ,
sum(COMMISSION_PCT) as total_commission_payout 
from emp_data 
group by DEPARTMENT_ID ;

-- Q3 : Display the department number and number of employees in each department.

select DEPARTMENT_ID , count(EMPLOYEE_ID) as num_employees from emp_data 
group by DEPARTMENT_ID ;


-- Q4 : Display the department number and total salary of employees in each department.

select DEPARTMENT_ID , sum(SALARY) as total_salary from emp_data 
group by DEPARTMENT_ID ;

-- Q5 : Display the employee's name who doesn't earn a commission. Order the result set without using the column name

select * from emp_data where COMMISSION_PCT is null order by 1 ;

-- Q6 : Display the employees name, department id and commission. If an Employee doesn't 
--      earn the commission, then display as 'No commission'. Name the columns appropriately.

select FIRST_NAME,DEPARTMENT_ID,COMMISSION_PCT ,
case 
when COMMISSION_PCT is null then 'No Commission'
else 'commission' 
end as COMMISSION_PCT 
from emp_data ;


-- Q7 : Display the employee's name, salary and commission multiplied by 2. If an Employee 
--      doesn't earn the commission, then display as 'No commission. Name the columns appropriately.

SELECT FIRST_NAME,SALARY,
CASE
WHEN COMMISSION_PCT IS NOT NULL THEN COMMISSION_PCT * 2
ELSE 'No commission' 
END AS appropriately
FROM emp_data ;

-- Q8 :  Display the employee's name, department id who have the first name same as another employee in the same department

select  FIRST_NAME,DEPARTMENT_ID from emp_data 
where FIRST_NAME = FIRST_NAME 
and EMPLOYEE_ID != EMPLOYEE_ID 
order by DEPARTMENT_ID , FIRST_NAME ;

-- Q9 : Display the sum of salaries of the employees working under each Manager.

select MANAGER_ID , sum(SALARY) as total_salary 
from emp_data group by MANAGER_ID ;

-- Q10 : Select the Managers id, the count of employees working under and the department ID of the manager.

select MANAGER_ID , count(EMPLOYEE_ID) as emp_count ,DEPARTMENT_ID 
from emp_data 
group by MANAGER_ID,DEPARTMENT_ID ;

-- Q11 : Select the employee name, department id, and the salary. Group the result with the 
--       manager name and the employee last name should have second letter 'a! 




-- Q12 : Display the average of sum of the salaries and group the result with the department id. Order the result with the department id. 

SELECT DEPARTMENT_ID, AVG(total_salary) AS average_salary
FROM (
    SELECT DEPARTMENT_ID, SUM(salary) AS total_salary
    FROM emp_data
    GROUP BY DEPARTMENT_ID
) AS department_salaries
GROUP BY DEPARTMENT_ID
ORDER BY DEPARTMENT_ID;

/*select DEPARTMENT_ID ,avg(SALARY) as avg_salary from emp_data
group by DEPARTMENT_ID 
order by DEPARTMENT_ID ; */

-- Q13 : Select the maximum salary of each department along with the department id.

SELECT DEPARTMENT_ID, MAX(SALARY) AS max_salary
FROM emp_data
GROUP BY DEPARTMENT_ID;

-- Q14 : Display the commission, if not null display 10% of salary, if null display a default value 1.

SELECT EMPLOYEE_ID,
CASE
     WHEN COMMISSION_PCT IS NOT NULL THEN salary * 0.10
	 ELSE 1
     END AS commission_result
FROM emp_data 
order by EMPLOYEE_ID;






