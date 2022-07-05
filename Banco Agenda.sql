create database workbank1;
use workbank1;
create table pessoas (id int not null primary key auto_increment, nome varchar(70) not null, datanasc date not null);
select * from pessoas;
insert into pessoas (nome , datanasc) value ('Algum Nome Bom', '2004-06-04');
