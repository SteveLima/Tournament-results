-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP view player_wins;

Drop table Matches cascade;

Drop table Players ;




CREATE table Players (ID serial primary key, fullname text) ;

CREATE table Matches (match_ID serial primary key, winner integer references Players(ID), loser integer references Players(ID) ); 


 CREATE VIEW player_wins AS
 		SELECT players.id, players.fullname,
       (SELECT Count(matches.winner)
        FROM   matches
        WHERE  matches.winner = players.id) AS wins,
       (SELECT Count(matches.match_ID)
        FROM   matches
        WHERE  matches.loser = players.id
                OR matches.winner = players.id) AS matches
FROM  players


