-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players(
    id serial primary key,
    name text
);

CREATE TABLE matches(
    p1 integer references players(id),
    p2 integer references players(id),
    winner integer references players(id)
);

CREATE VIEW matchesPerPlayer AS
    SELECT id, COUNT(players.id)::integer AS played
        FROM players, matches
        WHERE players.id = matches.p1 OR players.id = matches.p2
        GROUP BY id
        ORDER BY played DESC
;


CREATE VIEW winsPerPlayer AS
    SELECT id, COUNT(matches.winner)::integer AS wins
        FROM matches, players
        WHERE players.id = matches.winner
        GROUP BY id
        ORDER BY wins DESC
;

CREATE VIEW standings AS
    SELECT p.id, p.name,
    CASE WHEN w.wins IS NULL THEN 0 ELSE w.wins END,
    CASE WHEN m.played IS NULL THEN 0 ELSE m.played END
    FROM players p
    LEFT JOIN winsPerPlayer w ON p.id = w.id
    LEFT JOIN matchesPerPlayer m ON p.id = m.id
    ORDER BY wins DESC
;
