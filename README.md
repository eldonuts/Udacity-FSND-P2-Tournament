# Udacity FSND - Project 2

#### Description
This project was created as part of the Udacity Full Stack Web Developer Nanodegree. It's purpose is to interface with a PSQL database and keep tracking of players, standings and match ups for a tournament.

*Note: Code currently only supports even pairings*

#### Setup
1. Ensure Python 2.7 and psql are installed.
2. Clone the git repo to a local directory.
3. Open psql from terminal.
4. Run: \i tournament.sql to create the database.
5. You can now play around with the tournament.py file

#### Core Files
* **tournament.sql** Holds the database schema/commands to create the database and all tables/views used by this project
* **tournament.py** Hols all of the functions that are needed to run the tournament

#### Available Functions
* **connect** Connect to the PostgreSQL database.  Returns a database connection.
* **deleteMatches** Remove all the match records from the database.
* **deletePlayers** Remove all the player records from the database.
* **countPlayers** Returns the number of players currently registered.
* **registerPlayer** Adds a player to the tournament database.
* **playerStandings** Returns a list of the standings of each player including matches and wins.
* **reportMatch** Records the outcome of a single match between two players.
* **swissPairings** Returns the match ups for the next round.
