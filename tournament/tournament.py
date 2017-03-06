#!/usr/bin/env python
#tournament.py -- implementation of a Swiss-system tournament

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
"""Remove all the match records from the database."""

    db= psycopg2.connect("dbname=tournament")
    cur = db.cursor()
    cur.execute ("DELETE FROM Matches")
    cur.execute("UPDATE players SET wins = 0, matches = 0")
    db.commit()
    cur.close()



def deletePlayers():
    """Remove all the player records from the database."""

    db= psycopg2.connect("dbname=tournament")
    cur = db.cursor()
    cur.execute("DELETE FROM Players")
    db.commit()
    cur.close()

def countPlayers():
    """Returns the number of players currently registered."""
   
    db= psycopg2.connect("dbname=tournament")
    cur = db.cursor()
    cur.execute("SELECT count(*) FROM Players")
    player_s = cur.fetchone()[0]
    db.commit()
    cur.close()
    return player_s


def registerPlayer(name):
    """Adds a player to the tournament database.
    
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).

    """
   
    db= psycopg2.connect("dbname=tournament")
    cur = db.cursor()
    cur.execute("INSERT INTO Players(fullname) values(%s)",(name,))
    db.commit()
    cur.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    db= psycopg2.connect("dbname=tournament")
    cur = db.cursor()
    cur.execute("SELECT * FROM PLAYERS order by wins")
    ranks = []
    for row in cur.fetchall():
        ranks.append(row)
    db.commit()
    cur.close()
    return ranks

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
        record the wins on the Players table 
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    db= psycopg2.connect("dbname=tournament")
    cur = db.cursor()
    cur.execute("INSERT INTO Matches (winner,loser) values (%s,%s)",(winner,loser,))
    cur.execute("UPDATE players SET wins = wins+1, matches = matches+1 WHERE id =(%s)",(winner,))
    cur.execute("UPDATE Players SET matches = matches +1 WHERE id = (%s)",(loser,))
    db.commit()
    cur.close()


 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    db=psycopg2.connect("dbname=tournament")
    cur = db.cursor()
    pairi = []
    cur.execute("select id,fullname from players order by wins desc")
    value =cur.fetchall()
    for i in range(1, len(value), 2):
        one = value[i - 1]
        two = value[i]
        pairi.append((one[0], one[1], two[0], two[1]))
    for pairs in pairi:
        return pairi
    db.commit()
    cur.close()
   

