#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("UPDATE players SET matches = 0, wins = 0")
    conn.commit()
    conn.close()



def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE from players")
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM players")
    pairs = c.fetchall()[0][0]
    conn.close()
    return pairs




def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    name = bleach.clean(name)
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()

def playerStandings():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT id, name, wins, matches from players")
    pairs = c.fetchall()
    conn.close()
    return pairs
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


def reportMatch(winner, loser):
    conn = connect()
    c = conn.cursor()
    winner = bleach.clean(winner)
    loser = bleach.clean(loser)
    c.execute("UPDATE players SET wins = wins + 1 WHERE id = (%s)", (winner,))
    c.execute("UPDATE players SET matches = matches + 1 WHERE id = (%s)", (winner,))
    c.execute("UPDATE players SET matches = matches + 1 WHERE id = (%s)", (loser,))
    conn.commit()
    conn.close()
    
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
def findUniques(pairs): 
    pairings, uniqs = [], []
    for match in pairs:
        if (match[0] in uniqs) or (match[2] in uniqs):
            continue
        pairings.append(match)
        uniqs.extend(match)
    return pairings
    """Finds unique pairs from an array

    Args:
        pairs: an array with all possible parings of players with the same number of wins 
    """
def swissPairings():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT p1.id, p1.name, p2.id, p2.name FROM players p1, players p2 WHERE p1.wins = p2.wins AND p1.id != p2.id;")
    pairs = c.fetchall()
    conn.close()
    return findUniques(pairs)
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


