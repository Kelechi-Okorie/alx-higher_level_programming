-- creates db hbtn_0d_usa and table states
-- table schema (id INT UNIQUE AUTOGENERATE NOT NULL PRIMARY KEY, name VARCHAR(256))
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
-- create the table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa (id INT  UNIQUE AUTO_INCREMENT NOT NULL, name VARCHAR(256), PRIMARY KEY(id));