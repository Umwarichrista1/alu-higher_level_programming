-- Create the database hbtn_0d_usa, without failing if it already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the table states with an auto-generated primary key
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
