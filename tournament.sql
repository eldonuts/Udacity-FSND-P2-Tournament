-- Table definitions for the tournament project.


-- Connect to different database so tournament is free to drop.
\c postgres

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players(
    id serial primary key,
    name text
);

CREATE TABLE matches(
    match_id serial primary key,
    winner int references players(id),
    loser int references players(id)
);

CREATE VIEW matchesPerPlayer AS
    SELECT id, COUNT(players.id)::integer AS played
        FROM players, matches
        WHERE players.id = matches.winner OR players.id = matches.loser
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
