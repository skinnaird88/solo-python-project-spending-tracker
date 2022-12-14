DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    category VARCHAR(255)
);


CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    tag_id INT REFERENCES tags(id),
    amount INT,
    merchant_id INT REFERENCES merchants(id)
);