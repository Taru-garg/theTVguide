-- Creating ACTOR Table
-- drop table ACTOR;
create table ACTOR (
    act_id INT PRIMARY KEY,
    fname VARCHAR(40) NOT NULL,
    lname VARCHAR(40) NULL,
    gender CHAR(1) NOT NULL,
    dob DATE NULL,
    constraint chk_gen_act check(upper(gender) in ('M', 'F', 'O')),
    constraint chk_dob_act check(DATEDIFF(month, dob, GETDATE()) >= 1)
);
-- Test for Actor Table
-- truncate table ACTOR;
insert into actor
values
(1, 'Some', NULL, 'o', NULL),
-- (2, 'Some', 'Name', 'b', NULL), -- Error
(2, 'Some', 'Name', 'M', '2013-04-21');
-- (4, 'Some', 'Name', 'F', '2021-07-21') -- Error
select * from actor;
truncate table actor;

---------------------------------------------------------------------------------------

-- Creating DIRECTOR table
-- drop table DIRECTOR;
create table DIRECTOR (
    dir_id INT PRIMARY KEY,
    fname VARCHAR(40) NOT NULL,
    lname VARCHAR(40) NULL,
    gender CHAR(1) NULL,
    dob DATE NULL,
    constraint chk_gen_dir check(upper(gender) in ('M', 'F', 'O')),
    constraint chk_dob_dir check(DATEDIFF(month, dob, GETDATE()) >= 1)
)
-- Test for DIRECTOR table
insert into DIRECTOR
values
(1, 'Some', NULL, 'o', NULL),
-- (2, 'Some', 'Name', 'b', NULL), -- Error
(3, 'Some', 'Name', 'M', '2013-04-21');
-- (4, 'Some', 'Name', 'F', '2021-07-21') -- Error
select * from DIRECTOR;
truncate table DIRECTOR;

---------------------------------------------------------------------------------------

-- Creating table genres
-- drop table genres;
create table GENRES (
    gen_id INT PRIMARY KEY,
    genre VARCHAR(20) NOT NULL
);
-- Test for genres table
insert into GENRES
values
(1, 'Some Genre Name'),
--(2, NULL); -- Error
(3,'Horror'),
(4,'Sci-fi');

SELECT * FROM GENRES;
TRUNCATE TABLE GENRES;

---------------------------------------------------------------------------------------

-- Creating table movies
-- drop table movies
CREATE TABLE MOVIES (
    mov_id INTEGER PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    overview VARCHAR(MAX),
    length INTEGER,             --in minutes
    language VARCHAR(50),
    initial_release_date DATE,
    release_country VARCHAR(20)
);

--Test for table MOVIES
INSERT INTO MOVIES
VALUES
(1,'Fight Club',151,'English','1999-10-15','Canada'),
(2,'Shutter Island',139,'English','2010-02-13','Berlin');

SELECT * FROM MOVIES;

---------------------------------------------------------------------------------------

-- Creating table ratings
CREATE TABLE RATINGS (
    mov_id INTEGER NOT NULL,
    rev_id INTEGER NOT NULL,
    ratings DECIMAL(2,1),
    num_of_ratings INTEGER,
    FOREIGN KEY(mov_id) REFERENCES MOVIES(mov_id) ON DELETE CASCADE,
    UNIQUE(mov_id,rev_id)   
);

-- Test for table RATINGS
INSERT INTO RATINGS
VALUES
(1,21,8.8,1888),
(1,22,8.6,1889),
(2,21,9.1,2000),
(2,22,9.7,2001);

SELECT * FROM RATINGS;
TRUNCATE TABLE RATINGS;

---------------------------------------------------------------------------------------

-- Creating table cast
-- drop table cast
CREATE TABLE CAST (
    mov_id INTEGER,
    act_id INTEGER,
    PRIMARY KEY(mov_id, act_id),
    FOREIGN KEY (mov_id) REFERENCES MOVIES(mov_id) ON DELETE CASCADE,
    FOREIGN KEY (act_id) REFERENCES ACTOR(act_id) ON DELETE CASCADE
);

--Test for table CAST
-- All the values must exist in movies and actor table
INSERT INTO cast
VALUES
(1,2),
(1,1),
(2,1),
(2,2);

SELECT * FROM CAST;
TRUNCATE TABLE CAST;

---------------------------------------------------------------------------------------
-- Creating table movieImageData
-- drop table movieImageData

CREATE table movieImageData (
    mov_id INTEGER PRIMARY KEY,
    backdrop VARCHAR(40),
    poster VARCHAR(40),
    FOREIGN KEY (mov_id) REFERENCES MOVIES(mov_id) ON DELETE CASCADE
);

-- Test for movieImageData
-- mov_id must be in movie table

insert into movieImageData
values
(1, 'somebackdrop', 'someposter'),
(2, NULL, 'someposter');

select * from movieImageData;
truncate table movieImageData;

-- Deleting all values because they
-- have a column which is foreign key
delete from MOVIES where 1=1;
delete from actor where 1=1;
