CREATE DATABASE moviequest;
USE moviequest;

-- Changing groups for team as "groups" is a reserved word in MySQL
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    team INT,
    movies_watched TEXT,
    profile_picture VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE movies (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    year VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    director VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE groups (
    id INT NOT NULL AUTO_INCREMENT,
    group_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE group_users (
    id INT NOT NULL AUTO_INCREMENT,
    group_id INT NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (group_id) REFERENCES groups(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
