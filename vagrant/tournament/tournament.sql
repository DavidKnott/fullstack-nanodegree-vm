CREATE TABLE players (id SERIAL PRIMARY KEY,
                      name TEXT,
                      wins integer DEFAULT (0),
                      matches integer DEFAULT (0),
                      time TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

"""
  Creates sql table for players with the attributes:
  id: which is the way to keep track of them
  name: which is each players name
  wins: which is the number of wins each player has
  matches: which is the number of matches each player has played

"""
