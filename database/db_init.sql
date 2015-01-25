drop database if exists toutiao;

create database if not exists toutiao;
use toutiao;


drop table if exists Daily;
create table Daily
(
    Pub_Date date not null,
    -- 1 stands for completing retrieving
    -- -n stands for the times of failures of retrieving daily
    Status int not null,
    Raw_Html text null,
    primary key (Pub_Date)
);

drop table if exists Post;
create table Post
(
    Id int not null auto_increment,
    Head varchar(300) not null,
    Link varchar(500) not null,
    Site varchar(300) null,
    Byy varchar(300) null,
    Byy_Link varchar(500) null,
    Fromm varchar(300) null,
    Fromm_Link varchar(500) null,
    Pub_Date date not null,
    primary key (Id),
    foreign key (Pub_Date) references Daily(Pub_Date)
);


drop procedure if exists GetLastDate;
delimiter $$
create procedure GetLastDate(out _Pub_Date date)
begin
    select Max(Pub_Date) into _Pub_Date
    from toutiao.Daily;
end$$
delimiter ;

drop procedure if exists AddDaily;
delimiter $$
create procedure AddDaily(in Pub_Date date,
    in Status int,
    in Raw_Html text)
begin
    insert into toutiao.Daily(Pub_Date,
        Status,
        Raw_Html)
        values(Pub_Date,
            Status,
            Raw_Html);
end$$
delimiter ;


drop procedure if exists AddPost;
delimiter $$
create procedure AddPost(in Head varchar(300),
    in Link varchar(500),
    in Site varchar(300),
    in Byy varchar(300),
    in Byy_Link varchar(500),
    in Fromm varchar(300),
    in Fromm_Link varchar(500),
    in Pub_Date date
    )
begin
    insert into toutiao.Post (Head,
        Link,
        Site,
        Byy,
        Byy_Link,
        Fromm,
        Fromm_Link,
        Pub_Date)

        values (Head,
        Link,
        Site,
        Byy,
        Byy_Link,
        Fromm,
        Fromm_Link,
        Pub_Date);
end$$
delimiter ;
