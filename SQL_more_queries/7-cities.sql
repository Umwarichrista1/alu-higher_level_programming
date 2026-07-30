-- Create the database hbtn_0d_usa, without failing if it already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the table cities, linked to states by a foreign key
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
