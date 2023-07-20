-- Creates the database hbtn_0d_usa 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

--Activate Database
USE hbtn_0d_usa;

-- Creates the table states in data base hbtn_od_usa
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);
