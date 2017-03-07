-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP view player_info;

Drop table Matches cascade;

Drop table Players ;




CREATE table Players (ID serial primary key, fullname text) ;

CREATE table Matches (match_ID serial primary key, winner integer references Players(ID), loser integer references Players(ID) ); 


CREATE VIEW player_wins AS
		SELECT Players.ID, Players.fullname, count(Matches.winner) as wins,
		count(Matches.match_ID) as Matches from Players full join Matches on Players.ID = Matches.winner group by Players.ID;
