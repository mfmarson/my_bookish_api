CREATE TABLE authors (
id SERIAL PRIMARY KEY,
name TEXT NOT NULL);

CREATE TABLE titles (
id SERIAL PRIMARY KEY,
name TEXT NOT NULL);


CREATE TABLE directory (
id SERIAL PRIMARY KEY,
author_id INTEGER REFERENCES authors(id),
title_id INTEGER REFERENCES titles(id),
);






