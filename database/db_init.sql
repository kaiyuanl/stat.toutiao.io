create database if not exists toutiao;
use toutiao;

drop table if exists Post;

create table Post
(
    Id int not null auto_increment,
    Head varchar(300) not null,
    Link varchar(500) not null,
    Author varchar(300) null,
    Author_Link varchar(500) null,
    Submitter varchar(300) null,
    Submitter_Link varchar(500) null,
    Pub_Date date not null,
    primary key(Id)
);

drop procedure if exists GetLastDate;
delimiter $$
create procedure GetLastDate(out _Pub_Date date)
begin
    select Max(Pub_Date) into _Pub_Date
    from toutiao.Pub_Date;
end$$
delimiter;

drop procedure if exists AddPost;
delimiter $$
create procedure AddPost(in Head varchar(300),
    in Link varchar(500),
    in Author varchar(300),
    in Author_Link varchar(500),
    in Submitter varchar(300),
    in Submitter_Link varchar(500),
    in Pub_Date date
    )
begin
    insert into toutiao.Post value(Head,
        Link,
        Author,
        Author_Link,
        Submitter,
        Submitter_Link,
        Pub_Date);
end$$
delimiter;
