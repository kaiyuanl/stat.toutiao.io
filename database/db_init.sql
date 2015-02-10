DROP DATABASE IF EXISTS toutiao;

CREATE DATABASE IF NOT EXISTS toutiao;
USE toutiao;


DROP TABLE IF EXISTS Daily;
CREATE TABLE Daily
(
    Pub_Date DATE NOT NULL,

    -- 1 stands for completing crawling for this date
    -- -n stands for the times of failures of crawling for this date
    Status INT NOT NULL,
    Raw_Html TEXT NULL,
    PRIMARY KEY (Pub_Date)
);

DROP TABLE IF EXISTS Post;
CREATE TABLE Post
(
    Id INT NOT NULL AUTO_INCREMENT,
    Head VARCHAR(300) NOT NULL,
    Link VARCHAR(500) NOT NULL,
    Site VARCHAR(300) NULL,
    Byy VARCHAR(300) NULL,
    Byy_Link VARCHAR(500) NULL,
    Fromm VARCHAR(300) NULL,
    Fromm_Link VARCHAR(500) NULL,
    Pub_Date DATE NOT NULL,
    Raw_Html TEXT NULL,
    Click INT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (Pub_Date) REFERENCES Daily(Pub_Date)
);

DROP TABLE IF EXISTS Keyword;
CREATE TABLE Keyword
(
    Id INT NOT NULL AUTO_INCREMENT,
    Word TEXT NOT NULL,
    Count INT NOT NULL,
    PRIMARY key(Id)
);


