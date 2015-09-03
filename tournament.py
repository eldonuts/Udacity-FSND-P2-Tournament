#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from contextlib import contextmanager

def connect():
    #Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect("dbname=tournament")

@contextmanager
def with_cursor():
    #Decorator function to wrap up the connection and cursor.
    db = connect()
    cur = db.cursor()
    try:
        yield cur
    except:
        raise
    else:
        db.commit()
    finally:
        cur.close()
        db.close()

def deleteMatches():
    #Remove all the match records from the database.
    with with_cursor() as cur:
        cur.execute('DELETE FROM matches;')

def deletePlayers():
    #Remove all the player records from the database.
    with with_cursor() as cur:
        cur.execute('DELETE FROM players;')

def countPlayers():
    #Returns the number of players currently registered.
    with with_cursor() as cur:
        cur.execute('SELECT COUNT (*) FROM players;')
        result = cur.fetchone()
        result = int(result[0]) #Convert the count value from long to int
    return result

def registerPlayer(name):
    #Adds a player to the tournament database.
    with with_cursor() as cur:
        cur.execute('INSERT INTO players (name) VALUES (%s);',(name,))

def playerStandings():
    """
    Returns a list of the tuples containing player id, player name,
    win records and matches, sorted by wins.
    """
    with with_cursor() as cur:
        cur.execute('SELECT * FROM standings;')
        results = cur.fetchall()
    return results

def reportMatch(winner, loser):
    #Records the outcome of a single match between two players.
    with with_cursor() as cur:
        cur.execute('INSERT INTO matches (winner,loser) VALUES (%s,%s)',(winner,loser))
 
def swissPairings():
    """
    Returns pairs of players for the next round of a match
    in a list of tuples, each of which contains (id1, name1, id2, name2)
    """
    pairingList = [] #Create an empty pairing list to add to soon.
    standings = playerStandings() #Grab player standings from standings function (already sorted by wins)
    iterator = iter(standings) #Initialise iterator
    for player in iterator:
        p1 = player #Current Player
        p2 = next(iterator) #Next Player list
        pairing = tuple((p1[0],p1[1],p2[0],p2[1])) #Create tuple of pairing p1 vs p2
        pairingList.append(pairing) #Add tuple to list we created earlier
    return pairingList