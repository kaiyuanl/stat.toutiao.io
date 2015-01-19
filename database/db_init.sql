drop database if exists toutiao;

create database if not exists toutiao;
use toutiao;

drop table if exists Post;

create table Post
(
    Id int not null auto_increment,
    Head varchar(300) not null,
    Link varchar(500) not null,
    Site varchar(300) null,
    By varchar(300) null,
    By_Link varchar(500) null,
    Fromm varchar(300) null,
    Fromm_Link varchar(500) null,
    Pub_Date date not null,
    primary key(Id)
);

drop procedure if exists GetLastDate;
delimiter $$
create procedure GetLastDate(out _Pub_Date date)
begin
    select Max(Pub_Date) into _Pub_Date
    from toutiao.Post;
end$$
delimiter ;


drop procedure if exists AddPost;
delimiter $$
create procedure AddPost(in Head varchar(300),
    in Link varchar(500),
    in Site varchar(300),
    in By varchar(300),
    in By_Link varchar(500),
    in Fromm varchar(300),
    in Fromm_Link varchar(500),
    in Pub_Date date
    )
begin
    insert into toutiao.Post value(Head,
        Link,
        Site,
        By,
        By_Link,
        Fromm,
        Fromm_Link,
        Pub_Date);
end$$
delimiter ;
