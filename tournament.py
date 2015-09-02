#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    #Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    #Remove all the match records from the database.
    db = connect()
    cur = db.cursor()
    cur.execute('DELETE FROM matches;')
    db.commit()
    db.close()

def deletePlayers():
    #Remove all the player records from the database.
    db = connect()
    cur = db.cursor()
    cur.execute('DELETE FROM players;')
    db.commit()
    db.close()

def countPlayers():
    #Returns the number of players currently registered.
    db = connect()
    cur = db.cursor()
    cur.execute('SELECT COUNT (*) FROM players;')
    result = cur.fetchone()
    result = int(result[0]) #Convert the count value from long to int
    db.close()
    return result

def registerPlayer(name):
    #Adds a player to the tournament database.
    db = connect()
    cur = db.cursor()
    cur.execute('INSERT INTO players (name) VALUES (%s);',(name,))
    db.commit()
    db.close()

def playerStandings():
    """
    Returns a list of the tuples containing player id, player name,
    win records and matches, sorted by wins.
    """
    db = connect()
    cur = db.cursor()
    cur.execute('SELECT * FROM standings;')
    results = cur.fetchall()
    db.close()
    return results

def reportMatch(winner, loser):
    #Records the outcome of a single match between two players.
    db = connect()
    cur = db.cursor()
    cur.execute('INSERT INTO matches (p1,p2,winner) VALUES (%s,%s,%s)',(winner,loser,winner))
    db.commit()
    db.close()
 
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