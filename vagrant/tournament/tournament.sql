-- Clear out any previous DB.
DROP DATABASE IF EXISTS tournament;

-- Create DB.
CREATE DATABASE tournament;

-- Connect to the DB before creating tables.
\c tournament;

-- Creates sql table for players with the attributes:
-- id: which is the way to keep track of them
-- name: which is each players name
-- wins: which is the number of wins each player has
-- matches: which is the number of matches each player has played

CREATE TABLE players (id SERIAL PRIMARY KEY,
                      name TEXT,
                      wins integer DEFAULT (0),
                      matches integer DEFAULT (0),
                      time TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

