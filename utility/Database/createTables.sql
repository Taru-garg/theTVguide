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
(3, 'Some', 'Name', 'M', '2013-04-21');
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
(1, 'Some Genre Name');
-- (2, NULL); -- Error

---------------------------------------------------------------------------------------

