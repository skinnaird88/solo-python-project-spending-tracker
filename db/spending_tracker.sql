DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    amount INT
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255)
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    tag VARCHAR REFERENCES tags (id) ON DELETE CASCADE
);
