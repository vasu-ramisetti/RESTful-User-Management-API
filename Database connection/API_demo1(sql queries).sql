create database api_demo1;
use api_demo1;
create table users(
id int auto_increment primary key,
name varchar(100),
email varchar(100)
);
insert into users(name,email) values
('tiru','tiru@example.com'),
('vasu','vasu@example.com');

select * from users