-- create tables


CREATE TABLE IF NOT EXISTS second_table
(
    id INT,
    name VARCHAR(256) NOT NULL,
    score INT
);

INSERT INTO second_table(id, name, score) VALUES
    (1,'John',10),
    (2,'Alex',10),
    (3,'Bob',10),
    (4,'George',10);