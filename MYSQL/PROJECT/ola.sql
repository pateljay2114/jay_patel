create database ola;
use ola ;

create table driver
(
 driver_id int ,
 driver_name varchar(20) ,
 fare int ,
 journey varchar(23),
 driver_otp int primary key,
 driver_date datetime ,
 available_vehicle varchar(20)
 ) ;
 
 create table customer
 (
  customer_id int ,
  customer_name varchar(14) ,
  customer_otp int primary key ,
  journey varchar(34) ,
  foreign key customer(customer_otp) references driver(driver_otp) 
  );
  
  
select * from driver
inner join customer
on driver.driver_otp= customer.customer_otp ;
 
select * from driver
left join  customer
on driver.driver_otp= customer.customer_otp ; 

select * from driver
right join customer
on driver.driver_otp= customer.customer_otp ;

 