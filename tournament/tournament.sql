-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE table Players (ID serial primary key, fullname text, wins integer default 0, matches integer default 0) ;

CREATE table Matches (match_ID serial, winner integer references Players(ID), loser integer references Players(ID) ); 

