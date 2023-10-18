-- creates db hbtn_0d_usa and table cities
-- The script should not fail if db or table exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- cities description (id, state_id, name)
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL, name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id))