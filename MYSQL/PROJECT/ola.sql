create database ola;
use ola ;

create table driver
(
 driver_id int primary key ,
 driver_name varchar(20) ,
 fare int ,
 available_vehicle varchar(20)
 ) ;
 
 create table customer
 (
  customer_id int primary key ,
  customer_name varchar(14) ,
  pick_up varchar(15) ,
  drop_off varchar(15),
  foreign key customer(customer_id) references driver(driver_id) 
  );
  
  
select * from driver
inner join customer
on driver.driver_id= customer.customer_id ;
 
select * from driver
left join  customer
on driver.driver_id= customer.customer_id ; 

select * from driver
right join customer
on driver.driver_id= customer.customer_id ;

 